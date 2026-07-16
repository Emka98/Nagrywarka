import subprocess
import re
from typing import Generator
from objects import Disc, Distibution

def discList() -> list:
    result = subprocess.run(["lsblk", "-b", "-o", "TRAN,NAME,SIZE,MODEL"], capture_output=True, text=True)
    discs = []
    for line in result.stdout.splitlines():
        if "usb" in line.lower():
            parts = line.split()
            discs.append(Disc(node=parts[1], size=int(parts[2]), name=(" ".join(parts[3:]))))
    return discs

def cleanDisc(disc: Disc) -> Generator[float, None, int]:
    p1 = subprocess.Popen(
        ["dd", "if=/dev/zero", f"of=/dev/{disc.node}", "bs=1M", "count=1024","oflag=direct","status=progress"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        bufsize=0
    )
    
    buffor = ""
    
    while True:
        char = p1.stderr.read(1)
        
        if not char and p1.poll() is not None:
            break
        
        if char:
            if char in ('\r', '\n'):
                line = buffor.strip()
                match = re.search(r'^\d+', line)
                if match:
                    bajts = int(match.group())
                    # yield round(((skopiowane_bajty / disc.size)*100),2)
                    yield round(((bajts / 1_073_741_824)*100),2)
                buffor = ""
            else:
                buffor += char  
    p1.wait()
    return p1.returncode

def recordDisc(disc: Disc, distibution: Distibution) -> Generator[float, None, int]:
    p1 = subprocess.Popen(
        ["qemu-img", "convert", "-p", distibution.path, "-O", "raw", f"/dev/{disc.node}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        bufsize=0
    )
    
    buffor = ""
    pattern = re.compile(r'\(([\d.]+)/100%\)')
        
    while True:
            char = p1.stdout.read(1)
            
            if not char and p1.poll() is not None:
                break
                
            if char:
                if char in ('\r', '\n'):
                    line = buffor.strip()
                    
                    match = pattern.search(line)
                    if match:
                        procent = float(match.group(1))
                        yield procent
                        
                    buffor = ""
                else:
                    buffor += char
                    
    p1.wait()
    return p1.returncode

def formatToMSDOS(disc: Disc):
    
    p1 = subprocess.Popen(
        ["parted", f"/dev/{disc.node}", "mklabel", "msdos", "--script"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"
    )
    stdout1, stderr1 = p1.communicate()
    if p1.returncode != 0:
        print(f"Błąd Krok 1: {stderr1}")
        return False

    p2 = subprocess.Popen(
        ["parted", f"/dev/{disc.node}", "mkpart", "primary", "fat32", "1MiB", "100%", "--script"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"
    )
    stdout2, stderr2 = p2.communicate()
    if p2.returncode != 0:
        print(f"Błąd Krok 2: {stderr2}")
        return False

    p3 = subprocess.Popen(
        ["mkfs.vfat", "-F", "32", f"/dev/{disc.node}1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"
    )
    stdout3, stderr3 = p3.communicate()
    if p3.returncode != 0:
        print(f"Błąd Krok 3: {stderr3}")
        return False

    return 1

import subprocess
import re
from typing import Generator
from objects import Disc, Distibution
from collections import deque

def discList() -> list:
    result = subprocess.run(["lsblk", "-b", "-o", "TRAN,NAME,SIZE,MODEL"], capture_output=True, text=True)
    discs = []
    for line in result.stdout.splitlines():
        if "usb" in line.lower():
            parts = line.split()
            discs.append(Disc(node=parts[1], size=int(parts[2]), name=(" ".join(parts[3:]))))
    return discs

def cleanDisc(disc: Disc, make_pation: bool) -> Generator[int, None, int]:
    
    processSteps = 3
    progress = 0
    
    #Remove format od disc
    try:
        subprocess.run(["sudo", 
                        "dd", 
                        "if=/dev/zero", 
                        f"of=/dev/{disc.node}", 
                        "bs=1M", 
                        "count=100", 
                        "status=progress"], check=True, capture_output=True, text=True)
        progress += 1
        yield int(progress / processSteps * 100)
        
        
    except subprocess.CalledProcessError as e:
        print(f"Błąd systemowy (kod {e.returncode}): {e.stderr}")
        raise e
        
    #Make partition
    try:
        subprocess.run(["sudo",
                        "partprobe", 
                        f"/dev/{disc.node}"])
        progress += 1
        yield int(progress / processSteps * 100)
    except subprocess.CalledProcessError as e:
        print(f"Błąd systemowy (kod {e.returncode}): {e.stderr}")
        raise e
    
    #Format FAT32
    subprocess.run(["sudo", "umount", f"/dev/{disc.node}"], check=False, stderr=subprocess.DEVNULL)

    try:
        subprocess.run([
            "sudo", 
            "mkfs.vfat", 
            "-I",                  
            "-F", "32", 
            "-n", f"{disc.name}",
            f"/dev/{disc.node}"
        ], check=True, capture_output=True, text=True)
        
        progress += 1
        yield int(progress / processSteps * 100)
        
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr if e.stderr else e.stdout
        print(f"Błąd systemowy formatowania (kod {e.returncode}): {error_msg.strip()}")
        raise e

def recordDisc(disc: Disc, distibution: Distibution) -> Generator[float, None, int]:
    p1 = subprocess.Popen(
        ["sudo", "qemu-img", "convert", "-p", distibution.path, "-O", "raw", f"/dev/{disc.node}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        bufsize=0
    )
    
    for line in p1.stdout:
        yield line
    

disc = Disc(node="sdb", name="Kutasek")
distibution = Distibution(path="/home/emil/Desktop/noble-server-cloudimg-amd64.img", name="noble-server-cloudimg-amd64.img")

for i in cleanDisc(disc, True):
    print(i)
    
for i in recordDisc(disc, distibution):
    print(i)
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

def cleanDisc(disc) -> Generator[float, None, None]:
    processSteps = 3
    progress = 0
    device_path = f"/dev/{disc.node}"

    try:
        subprocess.run(["umount", "-q", "-A", device_path], check=False)
        subprocess.run(f" umount -q {device_path}*", shell=True, check=False)

        subprocess.run([
            "dd", 
            "if=/dev/zero", 
            f"of={device_path}", 
            "bs=1M", 
            "count=100"
        ], check=True, capture_output=True, text=True)

        progress += 1
        yield float(progress / processSteps * 100)

    except subprocess.CalledProcessError as e:
        error_msg = e.stderr if e.stderr else e.stdout
        print(f"Błąd systemowy przy zerowaniu (kod {e.returncode}): {error_msg.strip()}")
        raise e
    
    try:
        subprocess.run(["partprobe", device_path], check=True, capture_output=True, text=True)
        
        progress += 1
        yield float(progress / processSteps * 100)

    except subprocess.CalledProcessError as e:
        error_msg = e.stderr if e.stderr else e.stdout
        print(f"Błąd systemowy partprobe (kod {e.returncode}): {error_msg.strip()}")
        raise e


    try:
        subprocess.run(["umount", "-q", "-A", device_path], check=False)

        subprocess.Popen(
            [

                "mkfs.vfat",
                "-I",
                "-F",
                "32",
                "-n",
                "Transbit",
                device_path,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        
        progress += 1
        yield float(progress / processSteps * 100)
        
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr if e.stderr else e.stdout
        print(f"Błąd systemowy formatowania (kod {e.returncode}): {error_msg.strip()}")
        raise e
    return

def recordDisc(disc: Disc, distibution: Distibution) -> Generator[float, None, None]:
    p1 = subprocess.Popen(
        ["qemu-img", "convert", "-p", distibution.path, "-O", "raw", f"/dev/{disc.node}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        bufsize=0
    )
    
    for line in p1.stdout:
        progress = re.findall(r"\d+\.?\d*", line)[0]
        yield float(progress)
    return


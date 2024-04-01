#forkprocess
import os
import subprocess

os.system("echo Hello from the other side! > test.txt")
subprocess.run(["notepad", "test.txt"])
returncode = subprocess.run(["ping","google.com"]).returncode
print("done")
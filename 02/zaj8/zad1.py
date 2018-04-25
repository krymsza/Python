#!/usr/bin/env python
import subprocess
import os

try:
    with open(os.devnull, 'w') as devnull:
        subprocess.check_call(["g++ p.cpp "], stderr = devnull, shell=True)
    subprocess.check_call(["./a.out"], shell=True)
except subprocess.CalledProcessError as e:
    print (e)

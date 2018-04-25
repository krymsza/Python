#!/usr/bin/env python
import subprocess
linia = '      K4'
tabCount = len(linia) - len(linia.lstrip('  '))
print(tabCount)

subprocess.call(['mkdir', 'K1'], shell = False)
subprocess.call(['mkdir', 'K1/K2'], shell = False)

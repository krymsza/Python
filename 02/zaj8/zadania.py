#!/usr/bin/env python
  
import subprocess
out1 = subprocess.call(['echo', ' Hello Word'], shell=False)
out2 = subprocess.check_output(['echo', ' Hello Word'], shell=False)
print(out1)
print(out2)

-----------

#!/usr/bin/env python
  
import subprocess
import os

with open (os.devnull, "w") as devnull:
     out1 = subprocess.call(['ech', ' Hello Word'], stderr = devnull, shell = True) #wywolanie z bledem, wyciszymy wyjscie bledu
    
out2 = subprocess.call(['ech', ' Hello Word'], shell = True)

try:
    out3 = subprocess.check_call(['ech', ' Hello Word'], shell = True) # rzuca wyjstek w przeciwienstwie up
except subprocess.CalledProcessError as e:
    print(e)
    
------------------

#!/usr/bin/env python
#encoding: utf-8
import sys
arg = sys.argv
znaki = arg[2]
if arg[1] != "-":
    with open(arg[1]) as f:   
        for line in f:
            res = line.split()
            for znak in res:
                if znak==znaki:
                    print line
                    break

else:
    linia = " "
    while(linia != ""):
        linia=raw_input()
        lin = linia.split()
        for i in lin:
            if i==znaki:
                print linia
                break

print("koniec")
        

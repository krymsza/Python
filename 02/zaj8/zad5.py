# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:24:32 2018

@author: kat
"""
def gen_slow(tekst):
    for slowo in tekst.split():
        yield((slowo, len(slowo)))

with open("plik4.txt") as f:
        tekst = f.read()

for item in gen_slow(tekst):
    print(item)

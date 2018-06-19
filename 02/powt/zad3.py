# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 17:39:46 2018

@author: kat
"""
import re
import urllib.request
import urllib.parse
import urllib.error

path = input("podaj adres: ")
response =  urllib.request.urlopen("http://"+path+"/")
tekst = response.read().decode('utf-8')
response.close()
napis=input("podaj szukane slowo: ")
wyrazenie=re.compile(napis)
sum = 0

for linie in tekst.split():
    if(re.match(wyrazenie, linie)):
        sum = sum +1

print (sum)

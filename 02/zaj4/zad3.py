#!/usr/bin/env python
#encoding: utf-8
import sys

slownik={}

with open(sys.argv[1], "r") as f:
	for line in f:
		for e in line.split():
			if(e in slownik):
				slownik[e] = slownik[e] + 1
			else:
				slownik[e] = 1

print slownik

#!/usr/bin/env python
#encoding: utf-8
napis = '''k1: w2
k2: w2
k3: w3
'''

def podz(napis):
	napis = napis.split("\n")
	slownik={}
	for i in napis:
		if i != "\n" and i != "":
			a,b=i.split(":")
			slownik[a]=b
	return slownik

print podz(napis)

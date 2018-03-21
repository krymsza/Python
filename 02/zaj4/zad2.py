#!/usr/bin/env python
#encoding: utf-8

def podz(nazwa):
	f = open(nazwa)
	napis = f.read()
	f.close()
	napis = napis.split("\n")
	slownik={}
	for i in napis:
		if i != "\n" and i != "":
			key,val=i.split(":")
			slownik[key]=val
	return slownik

print podz("zad2_test.txt")

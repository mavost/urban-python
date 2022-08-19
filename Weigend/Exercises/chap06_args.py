#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap06_args.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 10/10/2017
#------------------------------------------------------------
''' Python 3 main - a small piece of code
'''

def quer(zahl):
	zahl_s=str(zahl)
	res=0
	for digi in zahl_s:
		res+=int(digi)
	return res

def quersumme(*zahlen):
	res=0
	for zahl in zahlen:
		res+=quer(zahl)
	return res



def main():
	print(quersumme())
	print(quersumme(1,100,12123,223))
	print(quersumme(1,100,123))
	
	
main()

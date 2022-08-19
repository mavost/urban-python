#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap06_asgn01.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 10/10/2017
#------------------------------------------------------------
''' this code hides meaning of a string variable
'''
from random import randint

def retletter(index):
	""" this function returns a letter based on it's index
	
	index <int>
	Returns encrypted message <string>
	No side effects
	MvS 10.10.2017
	"""
	mylist="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	return mylist[int(index)]
	

def hide_string(mystring,	#plain message
				strength=1	#encryption strength
				):
	""" this function encrypts a message one direction
	
	message <string>
	Returns encrypted message <string>
	No side effects
	MvS 10.10.2017
	"""
	instring=str(mystring).upper()
	res=""
	for bla in instring:
		res+=bla
		for foo in range(strength):
			res+=retletter(randint(0,25))
	#print(res)
	return res
	


def main():
	print(hide_string('Um acht Uhr an der Uhr.'))
	print(hide_string('Um acht Uhr an der Uhr.',4))

main()

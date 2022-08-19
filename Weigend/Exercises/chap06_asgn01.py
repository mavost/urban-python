#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap06_asgn01.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 10/10/2017
#------------------------------------------------------------
''' this code concatenates various string variable
'''

def konkat(*strings):
	""" this function concatenates strings
	
	Open number of parameters
	Returns String
	No side effects
	MvS 10.10.2017
	"""
	res=""
	for bla in strings:
		res+=str(bla)
	#print(res)
	return res
	


def main():
	print(konkat('a','b','c'))
	

main()

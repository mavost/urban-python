#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap06_asgn01.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 10/10/2017
#------------------------------------------------------------
''' this code calculates an approximation of the square root
'''

def refine(num,level=10):
	""" this function returns an approximation for a square root
	
	number to get the sqrt from <float>
	number of refinement levels <int>
	No side effects
	MvS 10.10.2017
	"""
	if level==1: return 1
	
	newval=0.5*(refine(num,level-1)+num/refine(num,level-1))
	return newval
	


def main():
	print(refine(2,5))
	print(refine(2))

main()

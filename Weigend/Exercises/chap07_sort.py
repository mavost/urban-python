#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap07_sort.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: xx/xx/2017
#------------------------------------------------------------
''' Python 3 main - a small piece of code
'''

from random import randint


def rand_list( min=10,      #minimum of range
			   max=100,     #maximum of range
			   elem=0		#number of elements
			   ):
	""" this function generates a list of random integer numbers
	
	Three parameters
	returns list
	MvS 11.10.2017
	"""
	if elem==0 or elem > int(max-min) : elem = int(max-min)
	
	res=[]
	b=randint(min,max)
	for a in range(elem):
		while b in res:			#unique values in list
			b=randint(min,max)
		else:
			res.append(b)
	return res
	
def bubblesort(s): #sorted list in argument
	if len(s) > 1:
		for i in range(len(s)-1):
			for j in range(len(s)-1):
				if s[j]>s[j+1]:
					s[j],s[j+1]=s[j+1],s[j]
			print(s)

def quicksort(s): #returns sorted list
	if len(s)>0:
		print("Sorting: ", s)
	if len(s)<=1: return s
	else:
		return quicksort([x for x in s[1:] if x < s[0]])\
		+ [s[0]]\
		+ quicksort([y for y in s[1:] if y >= s[0]])



bla=rand_list(10,20)


foo=bla[:]
print(foo)
quicksort(foo)
#print(quicksort(foo))
#bubblesort(foo)
#print(foo,)

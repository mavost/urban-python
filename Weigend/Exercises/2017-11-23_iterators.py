#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: 2017-11-23_iterators.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 23/11/2017
#------------------------------------------------------------
''' Python 3 main - Iterators
	find number permutations of a particular order which satisfy a arithmetical function
'''

import itertools


results = itertools.permutations(range(0,10),10)
out=[]
count=0
for result in results:
	count+=1
	#remove a few permutations
	if(result[6]>1):
		continue
	#remove a few permutations more
	if((result[2]+result[5])%10 != result[9]):
		continue
	#generate number format
	a=result[0]*100+result[1]*10+result[2]
	b=result[3]*100+result[4]*10+result[5]
	c=result[6]*1000+result[7]*100+result[8]*10+result[9]
	#check whether this works as planned
	#if(result[0]==0):
	#	print(a,'+',b,'=',c,sep='',end=', ')
	
	#check formula and add positives to list
	if(a+b==c):
		out.append((a,b,c))
		print(a,'+',b,'=',c,sep='',end=', ')
print()
print('Total of %i permutations and %i positives.'%(count, len(out)))


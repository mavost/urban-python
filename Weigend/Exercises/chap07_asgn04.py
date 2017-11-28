#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap07_asgn04.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 11/10/2017
#------------------------------------------------------------
''' Python 3 main - a small piece of code
'''


res=[]
for i in range(1,20):
	for j in range(1,20):
		for k in range(1,20):
			if(i*i+j*j==k*k or i*i==j*j+k*k or i*i+k*k==j*j): res.append((i,j,k))

print(res)
print()

dreiecke=set(frozenset((a,b,c))
					for a in range(1,20)
					for b in range(1,20)
					for c in range(1,20)
					if a**2+b**2==c**2)
for d in dreiecke:
	print(tuple(d), end=" ")

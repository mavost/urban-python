#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap08_asgn05.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 11/10/2017
#------------------------------------------------------------
''' Python 3 main - dictionaries counter
'''

def occurences(inputstr):
	res={}
	for a in inputstr:
		if a in res:
			res[a]+=1
		else:
			res[a]=1
	return res

out=occurences("Bananeneis")
for a,b in out.items():
	print(a,b)

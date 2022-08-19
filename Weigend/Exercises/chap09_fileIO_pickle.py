#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap09_fileIO_pickle.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 11/10/2017
#------------------------------------------------------------
''' Python 3 main - file input/output
'''

#convert backslash to slash er escape backslash in path names
#check file access permissions on directory
#check encoding settings

pathin="C:/Python36-32/workspace/data/NEWS.txt"
pathout="C:/Python36-32/workspace/data/News1.txt"

####################  Data  #######################
tel = {'Sabine':'89733',
		'Max':[897584,'0176 99494'],
		'Feuerwehr':'112',
		'Sabine':'112',}
tel1={}

####################  Main  #######################
import pickle
print("-----------Writing to a file using 'with... as... '-----------")
with open(pathout,'wb') as fileout:
	pickle.dump(tel, fileout)
	#filein.close() not required
	
print("-----------Reading from a file using 'with... as... '-----------")
with open(pathout,'rb') as filein:
	tel1=pickle.load(filein)
	#filein.close() not required
for a,b in tel1.items():
	print(a,":",b)
s=pickle.dumps(tel1)
print(str(s))
print(pickle.loads(s))




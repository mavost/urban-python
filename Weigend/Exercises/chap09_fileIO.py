#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap09_fileIO.py
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
path="C:/Python36-32/workspace/data/News1.txt"

try:
	#Reading
	datain=open(pathin,'r', encoding='utf8')
	print(datain.read(100))  #bytes to specify legth of read
	print(datain.seek(1000)) #jump to byte position
	print(datain.read(100))  #bytes to specify legth of read
	print(datain.readline()) #read one line and return string
	#print(datain.readlines()) #read line by line and return list of STR
	print(datain.tell())     #specify location of cursor
	#Writing
	dataout=open(path,'w')
	dataout.write("bananawrite\n")
	print('bananaprint',format(2/3,'8.3f'),end='\n',sep='\t',file=dataout)
	#only close call will save data to file - otherwise it's only buffered / use flush() to save while keeping open
except:
	print("File not found.")
finally:
	#put a backup option here
	datain.close()
	dataout.close()
	
	
####################  oder:  #######################
print("-----------Opening a file using 'with... as... '-----------")
with open(pathin,'r', encoding='utf8') as filein:
	print(filein.seek(10000))
	print(filein.read(500))
	#filein.close() not required
	



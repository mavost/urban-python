#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap14_system_functions.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 23/11/2017
#------------------------------------------------------------
''' Python 3 main - Overview of system functions
'''
TWIDTH=79								#Terminal width excluding EOL

#the outside world on python level
print("\n"+"python platform ".upper().ljust(TWIDTH,'#'))
print(TWIDTH*'#')

import sys
print('Your system platform is', sys.platform)
print('Python Version:\nPython '+sys.version)

print('\nPython standard modules:',sys.modules.keys())

print('\nFull link to python executable:',sys.executable)

print('\nDirectory path to python executable:',sys.exec_prefix)

#First element is the full path to the script file
print('\nList of command line arguments:')
for elem in sys.argv :
	print(elem)

print('\nList of module search paths:')
for elem in sys.path :
	print(elem)

#sys.stdin and sys.stdout can be diverted like in the unix shells

print('\nReferences to object "elem":', sys.getrefcount(elem))

#leave a script immediately with an optional integer error code / 0 := all is fine
#sys.exit(0)

#the outside world on operating system level
print("\n"+"operating system ".upper().ljust(TWIDTH,'#'))
print(TWIDTH*'#')

import os
owd=os.getcwd()
print('\nWorking directory:', owd)

print('\nMove on dir up the root (relatively): ', '..')
os.chdir('..')
print('New working directory:', os.getcwd())

print('\nMove to new location (absolutely): ', 'U:\\')
os.chdir('U:/')
print('New working directory:', os.getcwd())

print('\nMove to old location (absolutely): ', owd)
os.chdir(owd)
print('New working directory:', os.getcwd())

print('\nList dir contents:', os.listdir())
print('\nCheck path %s for dir type:' % (owd), os.path.isdir(owd))
print('\nCheck path %s for file type:' % (owd), os.path.isfile(owd))

print('\nAccess permissions:', os.listdir())
print('\nCheck path %s for write access:' % (owd), os.access(owd,os.W_OK))
#print('\nChange path %s to read access, only:' % (owd), os.chmod(owd,0o444))
#print('\nChange path %s to read,write,execute access:' % (owd), os.chmod(owd,0o777))

#print('\nCreate new directory: ', )
# newdir='tester'
# os.removedirs('c:/tmp/'+newdir)
# os.chdir('c:/tmp/')
# os.mkdir('tester',0o777)
# os.chdir('c:/tmp/'+newdir)
#print('Create and change to new directory:', 'c:/tmp/'+newdir)
#os.mkdir('tester',0o777)
#os.makedirs('tester',0o777)
#os.remove('tester.txt')
#os.removedirs('tester')
#os.rmdir('tester')
#os.rename('tester.txt','sister.txt')
#os.renames('tester.txt','sister.txt')

#create a file
#open(filename, 'a').close()

print('\nCreate file and new directory around it or touch an existing file: ')
def touch(mypath):
	basedir = os.path.dirname(mypath)
	if not os.path.exists(basedir):
		os.makedirs(basedir)
	with open(mypath, 'a'):
		os.utime(mypath, None)

print('\nList file sizes in python code dir: ', )
os.chdir(owd)
for file in os.listdir('.'):
	row='{file:>30}{bytes:>10} Byte'.format(file=file, bytes=os.path.getsize(file))
	print(row)

print('\nPath stuff: ', )
#os.path.abspath(path) 					#get absolute path from relative path
#os.path.join(path1, [path2], ...) 		#join paths
#os.path.normcase(path)			 		#convert path formatting to platform specs

print('\nSystem variables and environment: ', )
for var in os.environ:
	print(var, os.environ[var])
#os.environ['USERNAME']='Mickey'		#set existing(?) var
#os.getenv('USERNAME','Default')		#returns environment var or optional default if not found
#os.putenv('USERNAME','Minnie')			#set variable

print('\nSystematic layered inspection of a directory tree: ', )
#os.walk(path)							#search all subdirs

#the time module
print(TWIDTH*'#')
print("\n"+"the time module ".upper().ljust(TWIDTH,'#'))
print(TWIDTH*'#')

import time

print('Python knows three types of time format')
print('1) seconds since beginning of the epoch 1.1.1970')
print(time.time())				#UTC
print('2) tuple/struct time')
print(time.gmtime())			#UTC
print(time.localtime())			#local time
print('3) string format')
print(time.ctime())				#local time
print('Splitting off parts of the struct')
hour, minute, second=time.localtime()[3:6]
print('It is exactly {}:{}:{} local time'.format(hour, minute, second))


print('sleep timer')
time.sleep(6)					#sleep time in seconds

#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: 2017-10-16_threading.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 16/10/2017
#------------------------------------------------------------
''' Python 3 main - testing the threading module
'''

from threading import *
import time

def sleeper(i):
	print ("thread %d sleeps for %d seconds" % (i,i*10))
	time.sleep(5*i)
	print ("thread %d woke up" % i)

threads = []
#print(activeCount())

for i in range(10):
	print("start ",i)
	t = Thread(target=sleeper, args=(i,))
	threads.append(t)
	t.start()
	




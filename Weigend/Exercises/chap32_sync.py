#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap32_sanc.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 25/10/2017
#------------------------------------------------------------
''' Python 3 main - synchronisation without/with locking
'''
from multiprocessing import Process, Lock
from time import sleep

def f_nl(i):							# 2) no lock method
	print("Hallo! ",i)
	print("Das ist Prozess: ",i)

def f_l(l, i):							# 3) taking a lock object onboard
	l.acquire()
	print("Hallo! ",i)
	print("Das ist Prozess: ",i)
	l.release()

if __name__ == "__main__":				# 1) protects us from infinite recursion calls caused by sub-process p1
	for i in range(30):
		Process(target=f_nl, args=(i,)).start()	# 2) no locking results in chaos because of race condition
	sleep(10)
	lock=Lock()
	
	for i in range(30):
		Process(target=f_l, args=(lock,i)).start()	# 3) locking results in orderly resourse use

#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap32_queue-prod-cons.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 25/10/2017
#------------------------------------------------------------
''' Python 3 main - queue produce/consume
'''
from multiprocessing import Process, Queue
from time import sleep
from random import choice

BEGINNINGS=["Banana","Strawberry","Beet root"]
ENDINGS=["Shake","Juice","Beer"]

def produce(q,data):							# feed the queue with random fruit
	for a in range(3):
		q.put(choice(data))

def consume(q,data):							# take values out of the queue until it is empty
	while True:
		try:
			front=q.get(timeout=2)
			print(front, choice(data))
		except:
			break



if __name__ == "__main__":				# 1) protects us from infinite recursion calls caused by sub-process p1
	q=Queue(maxsize=3)
	producers=[Process(target=produce,args=(q,BEGINNINGS)) for i in range(2)]
	consumers=[Process(target=consume,args=(q,ENDINGS)) for i in range(2)]
	
	for p in producers+consumers: p.start()
	for p in producers+consumers: p.join()


#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap32_multiprocess.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 24/10/2017
#------------------------------------------------------------
''' Python 3 main - introduction to multiprocessing
'''
from multiprocessing import Process, Pipe, Queue, Pool
import os
from itertools import repeat
from time import time, sleep
 

def hello():
	print("Process-ID: %s, Name: %s" % (os.getpid(),__name__))

def squarelist(i):							# 3) example for sending data to processes one way
	#return [a*a for a in i]					#	return does not work
	print([a*a for a in i])						#	but data can be used

def squarelistpipe(i,order,pipe,length=0):			# 4) example for sharing data in processes both ways using Pipe
	print("Process-ID: %s, Name: %s" % (os.getpid(),__name__))
	sleep(length)
	pipe.send([order,[a*a for a in i]])			#	
	
def squarelistqueue(i,queue,length=0):				# 5) example for sharing data in processes both ways using Queue
	print("Process-ID: %s, Name: %s" % (os.getpid(),__name__))
	sleep(length)
	queue.put([a*a for a in i])

def squarelistpoolsimple(i):						# 6) example for a single argument use of Pool
	#print("Process-ID: %s, Name: %s" % (os.getpid(),__name__))
	sleep(.1)
	return i*i

def squarelistpoolmulti(i,length=0):				# 6) example for multi argument use of Pool
	#print("Process-ID: %s, Name: %s" % (os.getpid(),__name__))
	sleep(length)
	return i*i

if __name__ == "__main__":				# 1) protects us from infinite recursion calls caused by sub-processes p1/p2
	p1=Process(target=hello)
	p1.start()
	p2=Process(target=hello)
	p2.start()
	p1.join()							# 2) wait until p1 terminates and delete from process table
	p2.join()							#    wait until p2 terminates and delete from process table
	hello()
	print("####################################################\n"*2)
	mylist=list(range(1,100))			# 3) call two processes with two halves of a list
	print(mylist)
	p1=Process(target=squarelist, args=(mylist[:50],))	#	send half of the list into first process
	p1.start()
	p2=Process(target=squarelist, args=(mylist[50:],))	#	send other half of the list into second process
	p2.start()
	p1.join()
	p2.join()
	print("####################################################\n"*2)
	parent_conn, child_conn = Pipe()									# 4) call processes to work using pipes and parent_conn, child_conn
	p1=Process(target=squarelistpipe, args=(mylist[:50],0,child_conn))	#	send half of the list into first process together with pipe connection
	p1.start()
	p2=Process(target=squarelistpipe, args=(mylist[50:],1,child_conn))	#	send other half of the list into second process together with pipe connection
	p2.start()
	p1.join()															#	race condition, i.e. which process generates output first
	p2.join()
	result=[]
	result.append(parent_conn.recv())									#	two connections need two receiving calls
	result.append(parent_conn.recv())
	result.sort()														#	overhead to re-establish order, see, below
	res_merge=[]
	for row in result:
		res_merge+=row[1]
	print("Result:",res_merge)													#	observed that order of output is not maintained when running several times unless 
																		#	keeping control of processes numbers (e.g. by an higher order array)
	print("####################################################\n"*2)
	print("Process-ID: %s, Name: %s" % (os.getpid(),__name__))
	q = Queue()															# 5) call processes to work using FIFO i.e. queue
	p1=Process(target=squarelistqueue, args=(mylist[:50],q,1))				#	send half of the list into first process together with queue
	p1.start()
	p2=Process(target=squarelistqueue, args=(mylist[50:],q,2))				#	send other half of the list into second process together with queue
	p2.start()
	p1.join()
	result=q.get()															#	again race condition, i.e. which process generates output first
	print("First call in Queuetest:",result)
	result+=q.get()
	print("Second call in Queuetest:",result)
	p2.join()
#	result+=q.get()															#	would cause a hangup because there is no more data
#	print("Third call in Queuetest:",result)
	print("Result:",result)													#	observed that order of output is not maintained when running several times

	print("####################################################\n"*2)
	print("Process-ID: %s, Name: %s" % (os.getpid(),__name__))
	p1 = Pool()															# 6) distribute work on processes using pool class
	start=time()
	result_s=p1.map(squarelistpoolsimple,mylist)
	p1.close()
	p1.join()
	print(result_s, "Duration in parallel execution: ", time()-start)
	p2 = Pool()
	start=time()
	result_s=p2.starmap(squarelistpoolmulti,zip(mylist,repeat(.01)))
	p2.close()
	p2.join()
	print(result_s, "Duration in parallel execution with arg passing: ", time()-start)
	start=time()
	result_s=list(map(squarelistpoolsimple,mylist))						#	run a function with input
	print(result_s, "Duration in serial execution: ", time()-start)
	#result_m=p.starmap(squarelistpoolmulti, zip(mylist, repeat(10)))	#	zip second argument to each function call

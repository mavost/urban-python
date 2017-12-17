#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap20_threadGUI-Class.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 04/12/2017
#------------------------------------------------------------
''' Python 3 main - An example of using threads as inherited classes within tkinter lib
	-save tkinter code as *.pyw to supress console window
	
	https://pymotw.com/2/threading/

'''

from tkinter import *
from threading import Thread
from time import sleep
from random import randint

# logging output
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)


##############################################################################

class Counter (object):						# simple window with a status message and a button
											# 	to dynamically add threaded count down message labels
	def __init__(self):
		self.f = Tk()
		
		self.countdowns = []				# lists for Thread, stringVar, label
		self.numbers = []				
		self.labels = []				
		
		self.status = StringVar()
		Label(master=self.f, textvariable=self.status).pack()
		Button(master=self.f, command=self.startThread, text='Start!').pack()
		self.f.mainloop()
		
	def startThread(self):					# on buttonPush add another Thread, stringVar, label to parent list
		n=StringVar()
		t=Countdown(n)						# potentially name the Threads
		l=Label(master=self.f, textvariable=n).pack(side=RIGHT)
		self.countdowns.append(t)			# add to list
		self.numbers.append(n)
		self.labels.append(l)
		t.start()							# implicitely call run()
		#update Thread counter
		self.status.set('Number of threads started: '+str(len(self.countdowns)))
		
	

##############################################################################

class Countdown(Thread):					# inherited Thread class, defining stuff to do in run()
											# 	and calling start() on the instance will internally
											# 	invoke run()
	
	def __init__(self, number):				# send parent StringVar along
		Thread.__init__(self)
		self.number=number
	
	def run(self):							# add debug messages
		logging.debug('running')
		for i in range(11):					# count to ten and update the StringVar
			self.number.set(str(i))
			sleep(1)
		logging.debug('finished')

##############################################################################		
counter=Counter()
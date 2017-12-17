#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap20_threadGUI.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 04/12/2017
#------------------------------------------------------------
''' Python 3 main - An example of using threads within tkinter lib
	-save tkinter code as *.pyw to supress console window
'''

from tkinter import *
from time import *
import _thread

class Counter:
	def __init__(self):
		self.f = Tk()
		self.number = StringVar()
		Label(master=self.f, textvariable=self.number).pack()
		#Button(master=self.f, command=self.count, text='Start!').pack()	#does not work as 
																			#	intended because single threaded
																			#	program is held up completely 
																			#	by sleep()
		Button(master=self.f, command=self.countThreaded, text='Start!').pack()
		self.f.mainloop()
	
	def countThreaded(self):
		_thread.start_new_thread(self.count,())
	
	
	def count(self):
		for i in range(11):
			self.number.set(str(i))
			sleep(1)
		
counter=Counter()
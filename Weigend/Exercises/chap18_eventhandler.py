#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap18_eventhandler.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 04/12/2017
#------------------------------------------------------------
''' Python 3 main - An example of using the event handler of tkinter lib
	-save tkinter code as *.pyw to supress console window
'''

from tkinter import *

class Raster:
	def __init__(self):
		list=[(x,y) for x in range(10) for y in range(10)]
		self.window=Tk()
		for (i,j) in list:
			l=Label(master=self.window, width=2, height=1, bg='white')
			l.grid(column=i, row=j)
			l.bind(sequence='<Shift-Button-1>', func=self.shiftleftclick)
			l.bind(sequence='<Button-3>', func=self.rightclick)
			l.bind(sequence='<Double-Button-1>', func=self.leftdoubleclick)
		self.window.mainloop()
		
	def shiftleftclick(self, event):
		event.widget.config(bg='black')
		
	def rightclick(self, event):
		event.widget.config(bg='red')
		
	def leftdoubleclick(self, event):
		event.widget.config(bg='green')
	
	
raster=Raster()
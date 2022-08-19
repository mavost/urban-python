#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap15_asgn1.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 04/12/2017
#------------------------------------------------------------
''' Python 3 main - A light switch GUI using tkinter lib
	-save tkinter code as *.pyw to supress console window
'''

from tkinter import *

class Switch:
	def switch(self):
		if self.window.buttonstate.get()==1:
			self.window.buttonstate.set(0)
			self.window.label.config(text='Light Off',bg='black', fg='white')
		else:
			self.window.buttonstate.set(1)
			self.window.label.config(text='Light On',bg='white',fg='black')

	def __init__(self):
		self.window=Tk()
		self.window.title('Light Switch')						#window title
		self.window.buttonstate=IntVar()
		self.window.buttonstate.set(0)
		self.window.button=Button(text='On/Off',command=self.switch)
		self.window.label=Label(text='Light Off',width=40,height=20,bg='black', fg='white')
		self.window.label.pack()
		self.window.button.pack()
		self.window.mainloop()
	
	

switcher=Switch()
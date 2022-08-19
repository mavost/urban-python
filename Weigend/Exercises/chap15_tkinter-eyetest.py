#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap15_eyetest.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 30/11/2017
#------------------------------------------------------------
''' Python 3 main - on button push provide three by three row of random letter at decreasing size
'''

from tkinter import *
from random import choice

class EyeTest:
	letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	defaultrows=['A B C','D E F','G H I']
	def __init__(self):
		
		
		self.rerolls=0

		#class Tk
		self.window=Tk()
		self.window.title('Eye Test')						#window title
		self.window.geometry('500x400')						#window size

		#Instructions
		self.window.label = Label(master=self.window,
								text='Press button to change letters')
		self.window.label.pack()
		
		#Viewpane
		self.vars=[]
		#Generate label layout
		self.labels = [Label(master=self.window, font=('Arial',40),width=6),
						Label(master=self.window, font=('Arial',20),width=6),
						Label(master=self.window, font=('Arial',10),width=6)]
		for (row,label) in zip(EyeTest.defaultrows,self.labels):
			var=StringVar()									#build StringVar object as a dynamic text variable using getter/setter
			var.set(row)									#start with defaults
			self.vars.append(var)							#build list
			label.config(textvariable=var)					#update label linking text var
			label.pack()
		
		#Controls
		
		self.window.buttonvar=StringVar()
		self.window.buttonvar.set('New letters')
		self.window.button = Button(master=self.window,
								textvariable=self.window.buttonvar,
								command=self.reroll,
								width=20)
		self.window.button.pack(pady=10)
		#run
		self.window.mainloop()

	def reroll(self):
		self.rerolls+=1
		#How to change widget data displayed
		#option 1: resetting text display 
		self.window.label.config(text='Press button to change letters another time ('+str(self.rerolls)+')')#option 2: using textvariable encapsulation
		self.window.buttonvar.set('Reroll ('+str(self.rerolls)+')')
		for var in self.vars:								#update StringVars
			var.set(choice(EyeTest.letters)+' '+choice(EyeTest.letters)+' '+choice(EyeTest.letters))
			print(var.get())

eyetest=EyeTest()











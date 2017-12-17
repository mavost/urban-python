#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap16_calculator.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 04/12/2017
#------------------------------------------------------------
''' Python 3 main - A simple calculator using tkinter lib and the grid layout manager
	-save tkinter code as *.pyw to supress console window
'''

from tkinter import *

class Calculator(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.title('Calculator')
		self.end = 0
		self.display = Display(self)
		self.display.grid(column=0, row=0, sticky= E+W,
							columnspan=6, pady=5)
		keys=[  (0,1,'7'),(1,1,'8'),(2,1,'9'),(3,1,'/'),
				(0,2,'4'),(1,2,'5'),(2,2,'6'),(3,2,'*'),
				(0,3,'1'),(1,3,'2'),(2,3,'3'),(3,3,'-'),
				(0,4,'0'),(1,4,'%'),(2,4,'+')]
		for(i,j,letter) in keys:
			Key(self, letter).grid(column=i, row=j)
		Clear(self).grid(column=5, row=1)
		Calc(self).grid(column=5, row=2)
		self.mainloop()

class Key(Button):
	def __init__(self, parent, letter):
		Button.__init__(self, master=parent, text=letter,
						command=self.press, width=3)
		self.letter = letter
		self.parent = parent
	
	def press(self):
		d = self.parent.display
		if self.fenster.end:
			d.delete(0,len(d.get()))
			self.parent.end = 0
		d.append(self.letter)

class Key(Button):
	def __init__(self, parent, letter):
		Button.__init__(self, master=parent, text=letter,
						command=self.press, width=3)
		self.letter = letter
		self.parent = parent
	
	def press(self):
		d = self.parent.display
		if self.parent.end:
			d.delete(0,len(d.get()))
			self.parent.end = 0
		d.append(self.letter)

class Clear(Button):
	def __init__(self, parent):
		Button.__init__(self, master=parent, text='C',
						command=self.clear, width=3)
		self.display = parent.display
		
	def clear(self):
		self.display.clear()

class Calc(Button):
	def __init__(self, parent):
		Button.__init__(self, master=parent, text='=',
						command=self.calc, width=3)
		self.parent = parent
		
	def calc(self):
		if self.parent.end ==1:
			print(self.parent.display.get())
			lastindex=len(self.parent.display.get())
			for i, c in enumerate(self.parent.display.get()):
				if c=='=': 
					lastindex=i
					break
			self.parent.display.delete(lastindex,len(self.parent.display.get()))
			print(self.parent.display.get())
				
		result = eval(self.parent.display.get())
		end = len(self.parent.display.get())
		self.parent.display.insert(end, '='+str(result))
		self.parent.end = 1

class Display(Entry):
	def __init__(self, parent):
		Entry.__init__(self, master=parent, width=20)
	
	def append(self, letter):
		self.insert(len(self.get()), letter)

	def clear(self):
		self.delete(len(self.get())-1)
		
calculator=Calculator()
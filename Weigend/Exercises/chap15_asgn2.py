#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap15_asgn2.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 04/12/2017
#------------------------------------------------------------
''' Python 3 main - A currency conversion GUI using tkinter lib
	-save tkinter code as *.pyw to supress console window
'''

from tkinter import *

class Converter:
	RBMODES = [
        ('USD', 1.18),
        ('CAD', 1.46),
		('GBP', 0.89),
		]
	def convert(self):
		#get entry
		try:
			value=float(self.window.entry.get())
		except:
			value=0.00
		
		#look up radio button multiplier
		rbmode=self.window.buttonstate.get()
		for MODE in Converter.RBMODES:
			if(rbmode==MODE[0]):
				rbmulti=MODE[1]
				break
		#build output string and report
		output='Result: %.2f %s' % (value*rbmulti, rbmode)
		self.window.labelbottom.config(text=output)

	def __init__(self):
		self.window=Tk()
		self.window.title('Currency Converter')						#window title
		self.window.button=Button(master=self.window,text='Convert',command=self.convert)
		self.window.entry=Entry(master=self.window)
		self.window.labeltop=Label(master=self.window,justify=LEFT,text='Enter an amount of EUR currency,\n'+ 							'select currency to convert to\nand push button to proceed.',width=40)
		self.window.labelbottom=Label(master=self.window,text='Output', width=40)
		
		self.window.labeltop.pack()
		self.window.entry.pack(pady=10)

		self.window.buttonstate=StringVar()
		self.window.buttonstate.set(0)
		for MODE in Converter.RBMODES:
			rb=Radiobutton(master=self.window, text=MODE[0], value=MODE[0], 
				variable=self.window.buttonstate)
			rb.pack(anchor='w', padx=150, pady=4)
			if(MODE[0]=='USD'): rb.select()
		self.window.button.pack(pady=10)
		self.window.labelbottom.pack(pady=10)
		self.window.mainloop()
	
	

converter=Converter()
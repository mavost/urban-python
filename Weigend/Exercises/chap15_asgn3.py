#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap15_asgn3.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 04/12/2017
#------------------------------------------------------------
''' Python 3 main - A decision matrix GUI using tkinter lib
	-save tkinter code as *.pyw to supress console window
'''

from tkinter import *

class Converter:
	RBMODES = [
        ('Polyethylen (PE)', 1,1,0,1,1),
        ('Polystyrol (PS)', 0,1,1,0,0),
		('Polyvinylchloride (PVS)', 0,0,0,0,0),
		]
	
	CMODES = [
			('Smokes', 1, 0),
			('Drips', 1, 0),
			('Smells waxy', 1, 0),
			]
	
	def getId(self, list):
		state=0
		iter=1
		try:
			for readout in list:
				state+=iter*readout
				iter*=2
				#print(state, iter)
		except:
			state=0
		return state
	
	
	def evaluate(self):
		readlist=[self.window.rb1state.get(),self.window.rb2state.get(),\
					self.window.cb1state.get(),self.window.cb2state.get(),self.window.cb3state.get()]
		#get state
		readliststate=self.getId(readlist)
		resultstring='unknown'
		#compare to materials
		for MODE in Converter.RBMODES:
			if (self.getId(MODE[1:])==readliststate): 
				resultstring=MODE[0]
				break
		output='Result: material is %s' % (resultstring)
		self.window.labelbottom.config(text=output)

	def __init__(self):
		self.window=Tk()
		self.window.title('Plastic Identifier')						#window title

		self.window.labeltop=Label(master=self.window, justify=LEFT, text='Evaluation matrix to detect\n'+ 							'plastic material from its observed\nphysical properties',width=48)
		self.window.labeltop.pack()
		
		

		#Density property
		self.window.label1=Label(master=self.window, justify=LEFT, font=('Arial',12,'bold'), text='Floatation in water (density)')
		self.window.label1.pack()
		self.window.rb1state=IntVar()
		for MODE in [('floats',1), ('does not float',0)]:
			rb=Radiobutton(master=self.window, text=MODE[0], value=MODE[1], 
				variable=self.window.rb1state)
			rb.pack(anchor='w', padx=150, pady=4)
			if(MODE[1]==1): rb.select()

		#Flammability property
		self.window.label2=Label(master=self.window, justify=LEFT, font=('Arial',12,'bold'), text='Flammability')
		self.window.label2.pack()
		self.window.rb2state=IntVar()
		for MODE in [('burns',1), ('does not burn',0)]:
			rb=Radiobutton(master=self.window, text=MODE[0], value=MODE[1], 
				variable=self.window.rb2state)
			rb.pack(anchor='w', padx=150, pady=4)
			if(MODE[1]==1): rb.select()
		
		#Flammability extra properties
		self.window.label3=Label(master=self.window, justify=LEFT, font=('Arial',12,'bold'), text='Properties while burning')
		self.window.label3.pack()
			#set checkbuttons
		self.window.cb1state=IntVar()
		self.window.cb2state=IntVar()
		self.window.cb3state=IntVar()
		for var in [self.window.cb1state,self.window.cb2state,self.window.cb3state]:
			var.set('0')
		for MODE,var in zip(Converter.CMODES,[self.window.cb1state,self.window.cb2state,self.window.cb3state]):
			cb=Checkbutton(master=self.window, text=MODE[0], onvalue=MODE[1], offvalue=MODE[2], variable=var)
			cb.pack(anchor='w',padx=150)

		#Bottom control
		self.window.button=Button(master=self.window,text='Evaluate',command=self.evaluate)
		self.window.button.pack(pady=10)
		#Output with default
		self.window.labelbottom=Label(master=self.window,text='Output', width=40)
		self.window.labelbottom.pack(pady=10)
		
		self.window.mainloop()
	
converter=Converter()
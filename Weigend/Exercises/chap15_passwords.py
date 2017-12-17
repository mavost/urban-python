#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap15_passwords.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 30/11/2017
#------------------------------------------------------------
''' Python 3 main - password storage and gate using Entry class
'''

from tkinter import *


class PassWord:
	letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	defaultrows=['A B C','D E F','G H I']
	def __init__(self):
		
		
		self.users={'Tim':'mouse', 'admin':'root'}
		self.attempts=0

		#class Tk
		self.window=Tk()
		self.window.title('Login screen')					#window title
		self.window.geometry('300x200')						#window size

		#Instructions
		self.window.message=Label(master=self.window,
								text='Enter credentials')
		
		#Viewpane
		self.window.name = Entry(master=self.window)
		self.window.passw = Entry(master=self.window, show='#')
		self.window.loginbutton = Button(master=self.window,
								text='Login',
								command=self.login,
								width=20)
		self.window.name.pack(pady=10)
		self.window.passw.pack(pady=10)
		self.window.loginbutton.pack(pady=10)
		self.window.message.pack()
		#run
		self.window.mainloop()

	def login(self):
		cname=self.window.name.get()
		#if self.attempts>2: exit()
		if cname in self.users:
			if self.window.passw.get()==self.users[cname]:
				self.window.message.config(text='Welcome, '+cname+' !')
			else: 
				self.attempts+=1
				self.window.message.config(text='Wrong Password ('+str(self.attempts)+')')
		else:
			self.attempts+=1
			self.window.message.config(text='User not in database ('+str(self.attempts)+')')
		self.window.name.delete(0,END)
		self.window.passw.delete(0,END)

passw=PassWord()











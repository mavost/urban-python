#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: bmi06.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 26/10/2017
#------------------------------------------------------------
''' Python 3 main - object-oriented bmi evaluation in module saving to SQL db
'''
import sqlite3
import os.path

class User(object):
	def sayhi(self):
		print("User:", self.name, "is here.")
	
	def __init__(self):
		self.name=input('Name:')
		self.height=float(input('Körpergröße[cm]:'))
		print("Hallo", self.name)
	
	def __del__(self):
		print("User deleted:", self.name)

	def __str__(self):
		return "My name is User"+ self.name
	
class BMIcalc(object):
	def __init__(self):
		self.datastorage={}
		if not os.path.exists('data/bmi.db'):
			connection=sqlite3.connect('data/bmi.db')
			cursor=connection.cursor()
			cursor.execute('''CREATE TABLE bmirechner(name TEXT, bmi REAL)''')
		else:
			connection=sqlite3.connect('data/bmi.db')
			cursor=connection.cursor()
			cursor.execute('''SELECT name, bmi FROM bmirechner''')
			rows=cursor.fetchall()
			for row in rows:
				name=row[0]
				bmi=row[1]
				if name in self.datastorage:
					bmis=self.datastorage[name]
				else:
					bmis=[]
				bmis.append(bmi)
				self.datastorage.update({name:bmis})

	def calculate(self,hgt):
		weight=input('Gewicht[kg]:')
		if not len(weight):
			return
		return float(weight)/float(hgt)**2*10000

	def evaluate(self,b=20.0):
		if b>=25.0:
			print("Could be a sign of overweight. Please consult a doctor...")
		elif b<18.5:
			print("Could be a sign of starvation. Please consult a doctor...")
		else:
			print("Sounds healthy...")

	def append(self,n,b=0.0):
		if n in self.datastorage:
			bmis=self.datastorage[n]
		else:
			bmis=[]
		bmis.append(b)
		self.datastorage.update({n:bmis})
		connection=sqlite3.connect('data/bmi.db')
		cursor=connection.cursor()
		cursor.execute('''INSERT INTO bmirechner VALUES (?,?)''', (n,b))
		connection.commit()
		connection.close()

	def report(self):
		print("End of calculation")
		for i in self.datastorage.items():
			print(i)


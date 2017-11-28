#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: bmi05.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 26/10/2017
#------------------------------------------------------------
''' Python 3 main - object-oriented bmi evaluation in module saving to disk
'''
import os.path
from ast import literal_eval

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
		if os.path.exists('data/bmi.txt'):
			file=open('data/bmi.txt','r')
			for row in file:
				parts=row.split(':')
				name=parts[0]
				bmis=literal_eval(parts[1])
				self.datastorage.update({name:bmis})
			file.close()

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
		file=open('data/bmi.txt','w')
		for name in self.datastorage.keys():
			file.write(name+':[')
			bmis=self.datastorage[name]
			first=True
			for bmi in bmis:
				if not first:
					file.write(',')
				file.write(str(bmi))
				first=False
			file.write(']\n')
		file.close()

	def report(self):
		print("End of calculation")
		for i in self.datastorage.items():
			print(i)


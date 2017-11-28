#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: video04_object-or.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 26/10/2017
#------------------------------------------------------------
''' Python 3 main - object-oriented programming
'''

class User(object):
	def sayhi(self):
		print("User:", self.name, "is here.")
	
	def __init__(self, name, height=0.0):
		self.name=name
		self.height=height
		print("Initializing", name)
	
	def __del__(self):
		print("User deleted:", self.name)

	def __str__(self):
		return "My name is "+ self.name

class Admin(User):
	def __init__(self, name, height=0.0, password='1234'):
		self.name=name
		self.height=height
		self.password=password
		print("Initializing", name)
	def __str__(self):
		return "My name is Admin "+ self.name+" and my pw is: "+self.password


a=User('Hank', 180)
print(a)
a.sayhi()
del a
b=Admin("Tim")
print(b)




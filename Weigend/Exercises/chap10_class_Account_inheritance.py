#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap10_class_Account_inheritance.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 12/10/2017
#------------------------------------------------------------
''' Python 3 main - Inheritance
'''
from chap10_class_Ltender import LegalTender
import time

class Account(LegalTender):
	""" Specialization of Class LegalTender for 
		administration of current accounts
		Attributes:
		inherited: currency, _value, __exchangerates
		
		Public methods and overloads:
		inherited: __str__(), __add__(), getEuro(), showRates()
		overloaded: __str__()
		extensions: deposit(), withdraw(), printStatement()
	"""
	def __init__(self,currency,owner):
		LegalTender.__init__(self,currency,0.0)
		self.__owner=owner
		self.__statements=[str(self)]		#List of balance statement using overloaded string method
	
	def deposit(self,currency,value):
		depo=LegalTender(currency,value)
		self._value=(self+depo)._value
		logging=time.asctime() + ' ' + str(depo) +\
				' new balance:' + self.currency +\
				' ' + format(self._value,".2f")
		self.__statements += [logging]
		
	def withdraw(self,currency,value):
		self.deposit(currency,-value)
		return LegalTender(currency,value)
		
	def printStatement(self):
		for i in self.__statements:
			print(i)
		self.__statements = [str(self)]		#Hmmmmm
	
	def __str__(self):						#str overload
		return 'Account of ' + self.__owner +\
				':\nBalance on ' + time.asctime() +\
				': ' + format(self._value,'.2f') +\
				' ' + self.currency

		

print("============================================")
print("============================================")
print("Module: chap10_class_Account_inheritance.py")
print("============================================")
print("============================================")

Account.showRates() 			#call static method from child class
LegalTender.showRates()			#call static method from imported class

tomtest=Account("EUR","Thomas Edison")
tomtest.printStatement()
print('\n')
tomtest.deposit("JPY",10000)
tomtest.deposit("USD",100)
tomtest.printStatement()


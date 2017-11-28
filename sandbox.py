#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: sandbox.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: xx/xx/2017
#------------------------------------------------------------
''' Python 3 main - a small piece of code
'''

def arg_passer(**kwargs):
	for key,value in kwargs.items():
		print(key, value)


def round_t(rad=100,	#radius of the circle
			step=10     #reduction of the radius
			):
	""" this function draws a circle
	
	Two parameters
	Recursive call
	MvS 10.10.2017
	"""
	pass
	
def wertetabelle(anzahl=10, schritt = 0.5):
	print(anzahl,schritt)
	


def haengeAn(a,liste=[]):
	liste+=[a]
	print(liste)
	return liste


def main():
	name="Ion Tichy"
	description="Science Fiction comedy"
	year=2010
	sentence = name + " was made in " + str(year) + " and is a " + description
	print(sentence)

	choice = input('Enjoying the course? (y/n)')

	while choice not in ['y','n']:  # Fill in the condition (before the colon)
		choice = input("Sorry, I didn't catch that. Enter again: ")
		print(choice)
	wertetabelle(122)
	
	haengeAn(12)
	haengeAn(12)
	haengeAn(1122)
	haengeAn(12111)
	alt=haengeAn(66)
	print(alt)
	mylist=[1,1,1,1]
	haengeAn(liste=mylist,a=12111)
	
	hank={"A:":1,"B:":2,"C:":"elephant"}
	arg_passer(**hank)
	print(hank)
	arg_passer(a=2,b=222)


#define static variable	
class A:
	counter =0
	def callme (self):
		A.counter +=66
	def getcount (self):
		return self.counter  
	def __init__(self):
		A.counter+=10

print("no instance:", A.counter)

x=A()
print("first instance: ", x.getcount())
y=A()
print("second instance: ", y.getcount())
x.callme()
print("increment call: ", A.counter)
print("first instance: ",x.getcount())
print("second instance: ",y.getcount())



#main()



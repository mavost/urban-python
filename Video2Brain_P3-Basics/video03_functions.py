#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: video03_functions.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 26/10/2017
#------------------------------------------------------------
''' Python 3 main - implementing functions
'''

name=input('Name:')
print('Hallo ',name,' !', sep='')
height=float(input('Körpergröße[cm]:'))

def calculate(hgt):
	weight=input('Gewicht[kg]:')
	if not len(weight):
		return
	return float(weight)/float(hgt)**2*10000

def evaluate(b=20.0):
	if b>=25.0:
		print("Could be a sign of overweight. Please consult a doctor...")
	elif b<18.5:
		print("Could be a sign of starvation. Please consult a doctor...")
	else:
		print("Sounds healthy...")

def append(n,b=0.0):
	if n in datastorage:
		bmis=datastorage[n]
	else:
		bmis=[]
	bmis.append(b)
	datastorage.update({n:bmis})

def report():
	print("End of calculation")
	for i in datastorage.items():
		print(i)

datastorage={}
#endless loop until break condition is reached
while True:
	try:
		bmi=calculate(height)
		if not bmi:
			break
		evaluate(bmi)
		print('BMI:', '{:6.2f}'.format(bmi))
	except ValueError:
		print("Fehlerhafte Eingabe!")
		continue
	except ZeroDivisionError:
		print("Fehlerhafte Eingabe bei der Körpergröße!")
		continue
	except TypeError:
		print("Abbruch!")
	append(name,bmi)
report()




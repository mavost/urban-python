#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: video05_bmi-save.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 26/10/2017
#------------------------------------------------------------
''' Python 3 main - object-oriented bmi evaluation saving to disk
'''
from health.bmi05 import User, BMIcalc

bmicalc=BMIcalc()
user=User()
#endless loop until break condition is reached
while True:
	try:
		bmi=bmicalc.calculate(user.height)
		if not bmi:
			break
		bmicalc.evaluate(bmi)
		print('BMI:', '{:6.2f}'.format(bmi))
	except ValueError:
		print("Fehlerhafte Eingabe!")
		continue
	except ZeroDivisionError:
		print("Fehlerhafte Eingabe bei der Körpergröße!")
		continue
	except TypeError:
		print("Abbruch!")
	bmicalc.append(user.name,bmi)
bmicalc.report()

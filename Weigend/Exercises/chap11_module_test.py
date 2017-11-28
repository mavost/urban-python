#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap11_module_test.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 13/10/2017
#------------------------------------------------------------
''' Python 3 main - Class building blocks
'''


import sys
#sys.path.insert(0,'C:\\Python36-32\\workspace\\Weigend - Python 3 - Lernen und professionell anwenden\\Exercises\\modules')										#add extra path into search list for paths

print(sys.path)
try:
	from modules.legaltender import LegalTender
except:
	print("module not found")
	exit()

print()

print("==============LegalTender===================")
print()

LegalTender.showRates()												#call static method	


print()
print("============================================")
print("============================================")
hanks_dollars=LegalTender("USD",100)
peters_euros=LegalTender("EUR",230)
akiras_yen=LegalTender("JPY",10000)
akiras_yen.cl_currency=111											# dynamically create new variable in instance's namespace
akiras_yen.__class__.cl_currency=222								# set value of immutable variable in class namespace
akiras_yen.cl_translist.append(1)									# add one element to class transaction list
peters_euros.cl_translist.append(10)								# add another element to class transaction list
print()
print("============================================")
print("============================================")
volume=(hanks_dollars+peters_euros+akiras_yen)						#Plus operator in action
print("Currency in circulation converted to EUR equivalent: ", format(volume.getEUR(), "10.2f"))
print("Volume native wallet",volume)

print()
print("============================================")
print("============================================")
print("Hank's wallet",hanks_dollars)								#overloaded string operators in action
print("Peter's wallet"+str(peters_euros))
print("Akira's wallet"+" "+str(akiras_yen))

command = input("Enter Command for Testing: ")
while command != '':
	try:
		exec(command)
	except:
		print("Error: " + str(sys.exc_info()[0]))
	command = input("Enter Command for Testing: ")
print('End of Testing...')
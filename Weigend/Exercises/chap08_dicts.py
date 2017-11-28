#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap08_dicts.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 11/10/2017
#------------------------------------------------------------
''' Python 3 main - dictionaries
'''

tel = {'Sabine':'89733',
		'Max':[897584,'0176 99494'],
		'Feuerwehr':'112',
		'Sabine':'112',}


print(tel)
#del tel['Sabine']
print(tel)
t_new={}
t_new.update(tel)
del tel['Sabine']
print(tel)
print(t_new)
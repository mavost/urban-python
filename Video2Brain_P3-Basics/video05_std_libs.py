#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: video05_std_libs.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 26/10/2017
#------------------------------------------------------------
''' Python 3 main - use standard libs
'''

import os.path
import time

orig='data/bmi.db'					# result of working in SQL files, see chapter 6
if os.path.exists(orig):
	print("Path is present")
	if os.path.isfile(orig):
		print("...and is a file")
		print("Size:",os.path.getsize(orig))
		print("Last change:",time.ctime(os.path.getmtime(orig)))

import shutil
copy00='data/bmi.bak'

shutil.copy(orig,copy00)			#copy from source to destination
#shutil.move(orig,copy00)			#move from source to destination

if os.path.exists(orig):
	print("Original is present")
else:
	print("Original is not present")

if os.path.exists(copy00):
	print("Copy is present")
else:
	print("Copy is not present")

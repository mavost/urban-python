#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap10_asgn03.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 12/10/2017
#------------------------------------------------------------
''' Python 3 main - class model for "NewList"
'''

class NewList(list):
	""" Class NewList adds functionality to conventional list
		
		inherits the following objects from Thing:
		attributes:	lots
		methods: lots
		---------------------------------------
		attributes:	none
		methods:	range()
		overloads:	none
		
	"""
	
	def __init__(self, content=[]):
		content=list(content)
		list.__init__(self, content)
		
	
	def range(self):
		try:
			return max(self)-min(self)
		except:
			return 0
	
bla = NewList([1,45,1122,5.2323,-12.1])
print("range of bla is: ", bla.range())
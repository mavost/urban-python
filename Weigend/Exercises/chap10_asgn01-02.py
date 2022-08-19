#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap10_asgn01-02.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 12/10/2017
#------------------------------------------------------------
''' Python 3 main - class model for "Thing" and "Bar"
'''

class Thing(object):
	""" Class Thing models metal objects
		ClassAttributes:
		_density;
		InstanceAttributes: __mass; _symbol
		
		Public methods and overloads:
		getVolume(); getMass()
		__str__()
		
	"""
	
	_density={'Fe':('Iron',7.87),
			'Au':('Gold',19.32),
			'Ag':('Silver',10.5)}
	
	def __init__(self, symbol, mass):
		self.__mass=mass
		self._symbol=symbol

	
	def __str__(self):
		return 'A thing made of ' + Thing._density[self._symbol][0] +\
				' weighing ' + '{:8.2f}'.format(self.getMass()) + ' [g]\n' +\
				'with a volume of ' + '{:8.2f}'.format(self.getVolume()) +\
				' [ccm]'
		
	def getMass(self):
		return self.__mass
		
	def getVolume(self):
		return self.getMass()/Thing._density[self._symbol][1]
		
class Bar(Thing):
	""" Class Bar models metal objects
		
		inherits the following objects from Thing:
		attributes:	_density CAttrib; __mass, _symbol
		methods: getVolume(); getMass()
		---------------------------------------
		attributes:	__length, __width, __height
		methods:	none
		overloads:	__str__(), __ge__(), __eq__(), __gt__()
	"""
	def __init__(self, symbol, length, width, height):
		a = [length, width, height]							#bring dimension into right order according to attribute defs
		a.sort()
		self.__length=a[2]
		self.__width=a[1]
		self.__height=a[0]
		mass=Thing._density[symbol][1]*a[0]*a[1]*a[2]		#calculate mass from density x volume
		Thing.__init__(self, symbol, mass)					#instantiate parent class

	def __str__(self):
		return 'A bar made of ' + Thing._density[self._symbol][0] +\
				' weighing ' + '{:8.2f}'.format(self.getMass()) + ' [g]\n' +\
				'with a volume of ' + '{:8.2f}'.format(self.getVolume()) +\
				' [ccm]\n' + 'Dimensions (LxWxH):' + '{:8.2f}'.format(self.__length) + ' [cm] x' +\
				'{:8.2f}'.format(self.__width) + ' [cm] x' + '{:8.2f}'.format(self.__height) + ' [cm]'

	def __ge__(self,other):
		return self._Thing__mass>=other._Thing__mass
		
	def __gt__(self,other):
		return self._Thing__mass>other._Thing__mass

	def __eq__(self,other):
		return self._Thing__mass==other._Thing__mass
		
		
print("============================================")
print("============================================")
print("Module: chap10_asgn01.py")
print("============================================")
print("============================================")

goldcoin=Thing('Au',60)
print(goldcoin)
print("============================================\n")
silverbar=Bar('Ag', 10, 5, 8)
print(silverbar)
print("============================================\n")
ironbar=Bar('Fe',2,12,7)
print(ironbar)
print("============================================\n")
print("silverbar > ironbar? " + str(silverbar > ironbar))

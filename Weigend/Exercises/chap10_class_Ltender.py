#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap10_class_Ltender.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 12/10/2017
#------------------------------------------------------------
''' Python 3 main - Class building blocks
'''

class LegalTender(object):
	cl_currency="SSD"												# "static" immutable class variable
	cl_translist=[]													# "static" mutable class variable
	__exchangerates={"USD-EUR":0.84998,								# declare mangled "private" static variable
					"GBP-EUR":1.39480,
					"EUR-EUR":1.0,
					"JPY-EUR":0.007168}
	__allcurrencies=tuple(str(a[:3]) for a in __exchangerates.keys())
	def __init__(self,currency,value):
		self.currency=currency										# private variable
		self._value=float(value)									# private variable
	
	def getEUR(self):
		return self._value*LegalTender.__exchangerates[self.currency+"-EUR"]
	
	def add(self,leg_tend):
		sumEUR=self.getEUR()+leg_tend.getEUR() #convert to reference currency
		sumLT=LegalTender(self._currency,sumEUR/LegalTender.__exchangerates[self.currency+"-EUR"])
		return sumLT

	def __set_currency(self,value):
		if(value not in LegalTender.__allcurrencies):
			self._currency='EUR'
			print("WARNING: Currency not in my list, assuming EUR")
			#raise Exception("Currency not in my list")
		else:
			self._currency=value

	def __get_currency(self):
		return self._currency

	def __add__(self,leg_tend):									# overloading plus operator
		sumEUR=self.getEUR()+leg_tend.getEUR() #convert to reference currency
		sumLT=LegalTender(self._currency,sumEUR/LegalTender.__exchangerates[self.currency+"-EUR"])
		return sumLT

	def __str__(self):											# overloading string operator
		return "contains "+'{:010.2f}'.format(self._value) + " "+ \
				self.currency 
	
	def showRates():
		print("Today's exchange rates are:")
		for key,val in LegalTender.__exchangerates.items():
			print(key,": ",format(val,"10.5f"))
		
	currency = property(__get_currency, __set_currency)			#property declaration
	showRates=staticmethod(showRates)							#static method declaration

# module use:
# import.sys
# sys.path.append('module')										#add extra path into search list for paths
print("Importing "+ __name__)
if __name__ == '__main__':				#call test environment only if module is called standalone
	print()
	print("============================================")
	print("============================================")
	LegalTender.showRates()												#call static method	


	print()
	print("============================================")
	print("============================================")
	hanks_dollars=LegalTender("USD",100)
	peters_euros=LegalTender("EUR",230)
	akiras_yen=LegalTender("JPY",10000)
	print("Akiras wallet in JPY")
	print(format(akiras_yen._value,"10.2f"), akiras_yen._LegalTender__get_currency())		# call private variables(BAD)
	print("Akiras wallet in EUR")
	print(format(akiras_yen.getEUR(),"10.2f"), "EUR")

	print("Added 50 EUR")
	akiras_yen=akiras_yen.add(LegalTender("EUR",50))					# create anonymous object argument on the fly
	print("Akiras wallet in JPY")
	print(format(akiras_yen._value,"10.2f"), akiras_yen.currency)		# call private variables(BAD)
	print("Hanks plus Akiras wallet in EUR")
	print(format(akiras_yen.add(hanks_dollars).getEUR(),"10.2f"), "EUR")# call method on return value
	#print(akiras_yen._LegalTender__exchangerates)						# call mangled private variable
	#print(akiras_yen._LegalTender__allcurrencies)						# call mangled private variable

	akiras_yen.cl_currency=111											# dynamically create new variable in instance's namespace
	akiras_yen.__class__.cl_currency=222								# set value of immutable variable in class namespace
	akiras_yen.cl_translist.append(1)									# add one element to class transaction list
	peters_euros.cl_translist.append(10)								# add another element to class transaction list
	'''
	https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
	'''
	print()
	print("============================================")
	print("============================================")
	print("CLASS NAMESPACE:")
	for k,v in akiras_yen.__class__.__dict__.items():					#Access and list class namespace
		print(k,":\t",v)

	print()
	print("============================================")
	print("============================================")
	print("INSTANCE'S NAMESPACE:")
	for k,v in akiras_yen.__dict__.items():								#Access and list namespace of instance
		print(k,":\t",v)

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


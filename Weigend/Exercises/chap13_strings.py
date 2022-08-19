#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap13_strings.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 13/10/2017
#------------------------------------------------------------
''' Python 3 main - String Operations
'''

TWIDTH=79								#Terminal width excluding EOL


### FORMATTING
print("\n"+"formatting".upper().ljust(TWIDTH,'#'))
print(TWIDTH*'#')
a="banana split"
print(a.upper())						#Uppercase
print(a.rjust(TWIDTH,'-'))				#right justification with filler
print(a.center(TWIDTH))					#center with blanks
print(a.capitalize().ljust(TWIDTH,'#'))	#uppercase first letter in string, left justification with hash

b=' '.join([word.capitalize() for word in a.split()])
print(b)								#uppercase first letters in all words of string
print("The set {}={{A, B, C}}".format('X'))						#formatting using place holders
print("The train run in {} with a speed of {}".format('Greenland',15))
text="A {item} costs {price:->8.2f}EUR"							#:<filler-char><alignment <left, >right, ^center><digits including sign and decimals>
																#	<.><decimals><type f, d, x>
print(text.format(price=15.66666,item="can of spam"))			#number formatting

### LOGIC
print("\n"+"logic".upper().ljust(TWIDTH,'#'))
def strCheck(input):
	print(str("Verifying:\'"+input+"\'").ljust(TWIDTH,'#'))
	print("Extension check:\t", "Yes" if(input.lower().endswith('juice')) else "No" )			#One line ternary if using extensioncheck
	print("Alphanumeric check:\t", "Yes" if(input.isalnum()) else "No" )						#One line ternary if using alphanumeric check
	print("Literal check:\t", "Yes" if(input.isalpha()) else "No" )							#One line ternary if using literal check
	print("Number check:\t", "Yes" if(input.isdigit()) else "No" )							#One line ternary if using number check
	print("Lowercase check:\t", "Yes" if(input.islower()) else "No" )							#One line ternary if using lowercase check
	print("Uppercase check:\t", "Yes" if(input.isupper()) else "No" )							#One line ternary if using uppercase check
	
strCheck(input="102 dsds")
strCheck(input="dsDs")
strCheck(input="102")
strCheck(input="AMS")

### SPLITTING WORDS
input1="eat my shorts"
input2="B a n a n a"
input3="111#21344#Street###"
input4="\t eat my shorts"
input5="abababa"
print("\n"+"splitting and stripping".upper().ljust(TWIDTH,'#'))
print("Split:\t"+str(input1.split()))										# split string into words using separator def=' '
print("Split:\t"+str(input2.split()))										# split string into words using separator def=' '
print("Split:\t"+str(input3.split('#')))									# split string into words using separator def=' '
print("Lstrip:\t\'"+input4+"\'-->\'"+input4.lstrip()+"\'")					# strip from left side matching argument or remove all leading ' ' and '\t'
print("Lstrip:\t\'"+input1+"\'-->\'"+input1.lstrip('eat')+"\'")				# strip from left side matching characters or remove all leading ' ' and '\t'
print("Rstrip:\t\'"+input1+"\'-->\'"+input1.rstrip('orts')+"\'")			# strip from right side matching characters or remove all leading ' ' and '\t'
print("Strip:\t\'"+input4+"\'-->\'"+input4.strip('\t ets')+"\'")			# strip from both sides all matching char from list or ' ' and '\t'
print("Rstrip:\t\'"+input5+"\'-->\'"+input5.rstrip('abab')+"\'")			# strip from the right
print("Lstrip:\t\'"+input5+"\'-->\'"+input5.lstrip('bab')+"\'")				# strip from the left

### SEARCH AND REPLACE
input6="abababa"
search1='ba'
input7="111#21344#Street###"
search2='#S'
print("\n"+"searching and replacing".upper().ljust(TWIDTH,'#'))
print("Count:\t\'"+input6 + "\' contains \'" +search1+ "\' "+str(input6.count(search1))+" times")	# count occurence of search in input and return integer
print("Repla.:\t\'"+input6+"\'-->\'"+input6.replace('ab','ba')+"\'")								# replace old word by new word
print("Find:\t\'"+input7+"\'-->Found \'"+ search2 +"\' at index: "+str(input7.find(search2)))		# find returns index of first occurence of search term

### ENCODING
print("\n"+"encoding".upper().ljust(TWIDTH,'#'))
# for i in range(0x400, 0x4FF):															# output of cyrillic chars in unicode encoding
	# print(format(i,"X"),chr(i), end='\t')												# does not work in my windows 7 install
print()

word="Ärger"
word_bytes=word.encode()
print("\'"+word+"\' transforms to \'"+str(word_bytes)+"\' in bytecode")


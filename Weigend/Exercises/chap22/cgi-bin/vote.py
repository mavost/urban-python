#!/Python36-32/python.exe #Windows shebang 
#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chat.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 07/12/2017
#------------------------------------------------------------
''' Python 3 main - An example of collecting votes from a page using a form to get the data,
					a cookie to log a user, and a file to store/update the results 
					on a cgi-enabled http-server
					received from static page voting.html

	
https://docs.python.org/2.4/lib/node471.html

'''


import cgi

import cgitb									#debug mode on
cgitb.enable()

import os, pickle, http.cookies
from time import localtime

#constants
TEMPLATE = """{}
Content-type: text/html; char-set=utf-8;

<!DOCTYPE html>
<html>
  <meta http-equiv="content-type" content="charset=UTF-8" />
  <head> 
    <title> Voting page </title>
  </head>
  <body>
    <h2>Voting page</h2>
    <h3>{}</h3>
    Here are the current results for the question:<br>
    {}<br><br>{}<br><br>
    <a href="../index.html">back...</a>
  </body>
</html>"""
QUESTION = 'Do you like cats or dogs?'
ITEMS = ['Cats', 'Dogs']
VOTE_OK = 'Thank you for your vote.'
VOTE_NOT_OK = 'Sorry, but you already voted'
PATH = './XXX_vote.bin'

#local tuple time/date
time = localtime()
#my formatted data
mdate = '{:04d}-{:02d}-{:02d}'.format(time[0],time[1],time[2])
#read message / user and clear out garbage
file=PATH.replace('XXX',mdate)

class Counter(object):
	def __init__(self, file, items):
		self.file = file
		try:
			f = open(self.file, 'rb')
			self.data = pickle.load(f)
			f.close()
		except:											#file does not exist
			self.data={}
			for item in items:							#create and dump dictionary to new file
				self.data[item] = 0
			f = open(self.file, 'wb')
			pickle.dump(self.data, f)
			f.close()

	def vote(self, item):
		#an item receives a vote
		self.data[item] += 1
		f = open(self.file, 'wb')
		pickle.dump(self.data, f)
		f.close() 

	def __str__(self):
		#returns the formatted voting results for the HTML output
		result=''
		for item in self.data.keys():
			result += "<b>{}: </b>{} votes<br>\n".format(item, self.data[item])
		return result

class Ballot(object):
	def __init__(self):
		self.form = cgi.FieldStorage()
		self.counter = Counter(file, ITEMS)
		if not self.__voted_multi():
#		if True:																	#Cookies OFF
			if 'decision' in self.form.keys():			#check for form data from voting.html
				decision = self.form.getvalue('decision')
				self.counter.vote(decision)
			self.message = VOTE_OK
		else:
			self.message = VOTE_NOT_OK

	def __voted_multi(self):
		#returns true if I find a cookie value from a previous visit
		self.cookie = http.cookies.SimpleCookie()
		try:
			self.cookie.load(os.environ["HTTP_COOKIE"])
			return bool(self.cookie['votevisit'])		#which is always True if it exists
		except:
			self.cookie['votevisit'] = True
			return False

	def __str__(self):
		return TEMPLATE.format(self.cookie, self.message, QUESTION, self.counter)
#		return TEMPLATE.format(' ', self.message, QUESTION, self.counter)			#Cookies OFF

print(Ballot())

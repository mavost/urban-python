#!/Python36-32/python.exe #Windows shebang 
#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap23_http.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 08/12/2017
#------------------------------------------------------------
''' Python 3 main - Using the HTTP transfer library

	


'''

from http.client import HTTPConnection

'''
HTTPConnection object:
Methods
	request()
	getresponse() returns HTTP-Response object
	close()

HTTP-Response object:
Methods and attributes
	read()
	status
	reason

'''

connection = HTTPConnection('www.python.org')
connection.request('GET', '/index.html')				#GET or POST
response = connection.getresponse()

print(response.status, response.reason)
content = response.read()
connection.close()
print(content)

#results in status 301 - Moved Permanently

connection = HTTPConnection('localhost',8100)
connection.request('GET', '/index.html')				#GET or POST
response = connection.getresponse()

print(response.status, response.reason)
content = response.read()
connection.close()
print(content.decode("utf-8"))							#content in bytecode is converted to utf

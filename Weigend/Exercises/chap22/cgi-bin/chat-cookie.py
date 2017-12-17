#!/Python36-32/python.exe #Windows shebang 
#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chat-cookie.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 07/12/2017
#------------------------------------------------------------
''' Python 3 main - An example of building a chat room on a cgi-enabled http-server
					receiving data after choosing avatar in chat.html request
					and updating after each entry - using cookies for auto refresh
					--> unfortunately this doesnt work just yet
					
https://docs.python.org/2.4/lib/node471.html

'''


import cgi

import cgitb									#debug mode on
cgitb.enable()

import os
from http.cookies import SimpleCookie

from time import localtime, asctime
#local tuple time/date
time = localtime()
#my formatted time for message line
mtime = '{:02d}:{:02d}:{:02d}'.format(time[3],time[4],time[5])

#read message / user and clear out garbage

cookie=SimpleCookie()
form = cgi.FieldStorage()

try:
	cookie.load(os.environ["HTTP_COOKIE"])
	cookie["attempt"] = int(cookie["attempt"].value)+1
except:
	cookie["attempt"] = "1"

name = form.getvalue('name')
if name is None:
	name = 'Incognito'
	
message = form.getvalue('message')
if message is None:
	message = '...thinks...'

utime = form.getvalue('utime')
if utime is None:
	utime = asctime(time)


#  dumb reload, loosing all variables
#  <meta http-equiv="refresh" content="10; url=http://localhost:8100/cgi-bin/chat.py" content="charset=UTF-8" />
#  just static
#  <meta http-equiv="content-type" content="charset=UTF-8" />
#print output
TEMPLATE = """Content-type: text/html 
{}

<!DOCTYPE html>
<html>
  <meta http-equiv="content-type" content="charset=UTF-8" />
  <body>
	attempt {}
	<br><br>
    <a href="../index.html">back...</a>
  </body>
</html>"""

HTML = {ord('ä'): '&auml;', ord('ö'): '&ouml;', ord('ü'): '&uuml;',
		ord('Ä'): '&Auml;', ord('Ö'): '&Ouml;', ord('Ü'): '&Uuml;',
		ord('ß'): '&szlig;'}

output = TEMPLATE.format(cookie, cookie["attempt"].value).translate(HTML)
print(output)

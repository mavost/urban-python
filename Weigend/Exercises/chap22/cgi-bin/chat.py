#!/Python36-32/python.exe #Windows shebang 
#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chat.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 07/12/2017
#------------------------------------------------------------
''' Python 3 main - An example of building a chat room on a cgi-enabled http-server
					receiving data after choosing avatar in chat.html request
					and updating after each entry
	
https://docs.python.org/2.4/lib/node471.html

'''


import cgi

import cgitb									#debug mode on
cgitb.enable()

from time import localtime, asctime

#local tuple time/date
time = localtime()
#my formatted time for message line
mtime = '{:02d}:{:02d}:{:02d}'.format(time[3],time[4],time[5])
mdate = '{:04d}-{:02d}-{:02d}'.format(time[0],time[1],time[2])

#read message / user and clear out garbage
path='./{}_message.log'.format(mdate)
try:
	f = open(path, 'r')
	data = f.readlines()
	f.close()
except:											#file does not exist
	data=[]
	f = open(path, 'w')
	f.close()


form = cgi.FieldStorage()

try:
	name = form.getvalue('name')
	if name is None : name = 'Incognito'
except:
	name = 'Admin'
try:
	usertime = form.getvalue('usertime')
	if usertime is None : usertime = asctime(time)
except:
	usertime = asctime(time)+'*'
try:
	message = form.getvalue('message')
except:
	message = 'error'
if message is not None:							#if new message submitted, to chat
	new_row = '{}, {}: {}<br>\n'.format(mtime, name, message)
	data.append(new_row)
	f = open(path, 'a')
	f.write(new_row)
	f.close()

chatlines="".join(data[-10:])


#  dumb reload, loosing all variables
#  <meta http-equiv="refresh" content="10; url=http://localhost:8100/cgi-bin/chat.py" content="charset=UTF-8" />
#  just static
#  <meta http-equiv="content-type" content="charset=UTF-8" />
#print output
TEMPLATE = """Content-type: text/html; char-set=utf-8

<!DOCTYPE html>
<html>
  <meta http-equiv="content-type" content="charset=UTF-8" />
  <body>
    <h2>CGI chat room</h2>
    Welcome {}, you logged in on {}<br><br>
    Last ten messages:<br>
    {}
    <br><br>
    <form action="http://localhost:8100/cgi-bin/chat.py" method="post" >
    <!-- Open entries -->
    Your message:  <input type="text" name="message" maxlength=200 size=15> 
    <!-- Hidden variables -->
                 <input type="hidden" name="name" value="{}">
                 <input type="hidden" name="usertime" value="{}">
    <!-- Submit button -->
                 <input type="submit" value="Send/Reload">
    </form>
    <br>
    Current time: {}
	<br><br>
    <a href="../index.html">back...</a>
  </body>
</html>"""

HTML = {ord('ä'): '&auml;', ord('ö'): '&ouml;', ord('ü'): '&uuml;',
		ord('Ä'): '&Auml;', ord('Ö'): '&Ouml;', ord('Ü'): '&Uuml;',
		ord('ß'): '&szlig;'}

output = TEMPLATE.format(name, usertime, chatlines, name, usertime, asctime(time)).translate(HTML)
print(output)

#!/Python36-32/python.exe #Windows shebang 
#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: login.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 06/12/2017
#------------------------------------------------------------
''' Python 3 main - An example of using a script on a cgi-enabled http-server
					receiving data via login.html request
	
https://docs.python.org/2.4/lib/node471.html

'''


import cgi
import cgitb									#debug mode on
cgitb.enable()

form = cgi.FieldStorage()
#	getvalue(<name>) to receive None, value, or values(type(list)) --> needs handling later
#	getfirst(<name>) to receive None, value, or values[0]
#	getlist(<name>) to receive None, [value], or values(type(list))
#	keys() and [form.getlist/getfirst/...(key) or form[key] for key in form.keys()]

HTML = {ord('ä'): '&auml;', ord('ö'): '&ouml;', ord('ü'): '&uuml;'}

fname = form.getvalue('first_name')
name = form.getvalue('name')
passw = form.getvalue('pass')
radiovar = form.getvalue('decision')			#one option
checkvars = form.getvalue('food')				#several options
hiddenvar = form.getvalue('secret')

# create key/value table
vars1=', '.join(["fname", "name", "passw", "radiovar", "checkvars", "hiddenvar"])
vars2=[fname, name, passw, radiovar, checkvars, hiddenvar]
vars2=['None' if v is None else v for v in vars2]			#filter None type
vars2=['('+'&&'.join(v)+')' if type(v)==list else v for v in vars2]	#join sublists with different separator
vars2=', '.join(vars2)										#join main list

vars3=', '.join([v for v in form.keys()])
vars4=', '.join(['('+'&&'.join(form.getlist(v))+')' for v in form.keys()])

TEMPLATE = """Content-type: text/html; char-set=utf-8

<!DOCTYPE html>
<html>
  <meta http-equiv="content-type" content="charset=UTF-8" />
  <body>
    <h2>Login successful! Welcome, {} {}</h2>
    Values manually shaped in a list:<br>
    {}<br>
    {}<br>
    Values transmitted and read from dictionary:<br>
    {}<br>
    {}<br><br>
      <a href="../index.html">back...</a>
  </body>
</html>"""

output = TEMPLATE.format(fname, name, vars1, vars2, vars3, vars4).translate(HTML)
print(output)
#print(bug)
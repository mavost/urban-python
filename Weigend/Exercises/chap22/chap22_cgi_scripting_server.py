#!/Python36-32/python.exe #Windows shebang 
#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap22_cgi_scripting_server.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 06/12/2017
#------------------------------------------------------------
''' Python 3 main - An example of using a python-based cgi-enabled http-server
	
	

'''

from http.server import HTTPServer, CGIHTTPRequestHandler
address = ""
port = 8100
serveraddress = (address, port)
server = HTTPServer(serveraddress, CGIHTTPRequestHandler)
print('server start successful - access via {}:{}'.format(address, port))
server.serve_forever()

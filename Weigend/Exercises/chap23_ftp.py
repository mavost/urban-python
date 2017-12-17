#!/Python36-32/python.exe #Windows shebang 
#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap23_ftp.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 08/12/2017
#------------------------------------------------------------
''' Python 3 main - Using the FTP transfer library

	


'''

import ftplib

ftp =  ftplib.FTP('ftp.uni-koeln.de', 'anonymous', 'me@gmx.net')

ftp.retrlines('LIST')						#TEXT mode transfer of COMMAND to screen
mylist=[]
ftp.retrlines('LIST', mylist.append)		#TEXT mode transfer to variable
print(mylist)

ftp.cwd('adsm')								#change directory by relative path
ftp.quit()									#exit

ftp =  ftplib.FTP('taurus.caf.dlr.de', 'anonymous', 'me@gmx.net')
ftp.cwd('/put/wetterbilder/Germany')		#change directory by absolute path
ftp.retrlines('LIST')						#TEXT mode transfer of COMMAND to screen
f=open('data/ftp_wetterbild.jpg','wb')
ftp.retrbinary('RETR image1.jpg', f.write)
f.close()


#!/Python36-32/python.exe #Windows shebang 
#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap23_smtp.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 08/12/2017
#------------------------------------------------------------
''' Python 3 main - Using the SMTP library and tkinter to create a tiny mail client

	


'''

import smtplib
from tkinter import *

TEMPLATE = """From: {}
To: {}
Subject: {}
MIME-Version: 1.0
Content-Type: text/htmlContent-Transfer-Encoding: quoted-printable

{}"""

# SMTPSERVER = 'smtp.myprovider.de'
# SENDER = 'me@gmail.com'
# PASSWORD = '12345'

SMTPSERVER = 'smtp.myprovider.de'
SENDER = 'me@gmail.com'
PASSWORD = '12345'

class SMTPClient:
	def __init__(self):
		window=Tk()
		window.title('SMTP-Client v.0.1')
		Label(master=window, text='Recipient: ').grid(row=0, column=0)
		self.address = Entry(master=window, width=40)
		self.address.grid(row=0, column=1, pady=5)
		Label(master=window, text='Subject: ').grid(row=1, column=0)
		self.subject = Entry(master=window, width=40)
		self.subject.grid(row=1, column=1, pady=5)
		self.msgbody = Text(master=window, width=40, height=10)
		self.msgbody.grid(row=3, column=1, padx=5, pady=5)
		self.sending = Button(master=window, text='Send', command=self.__send)
		self.sending.grid(row=3, column=0, padx=5)
		self.sender = SENDER
		window = mainloop()

	def __send(self):
		server = smtplib.SMTP(SMTPSERVER)
		server.login(SENDER, PASSWORD)
		server.set_debuglevel(1)
		content = self.msgbody.get('1.0', END)
		message = TEMPLATE.format(SENDER, self.address.get(), self.subject.get(),
							content)
		server.quit()

SMTPClient()
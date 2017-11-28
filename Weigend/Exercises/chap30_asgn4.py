#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap30_asgn4.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 24/10/2017
#------------------------------------------------------------
''' Python 3 main - decipher secret message
'''
from tkinter import filedialog #bug/missing import
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
LETTERS = " abcdefghijklmnopqrstuvwxyzßäöü"

class App:
	def __init__(self):
		self.window = Tk()
		self.label = Label(self.window)
		self.label.pack()
		self.text = Text(self.window, width=50, height=5,
						 wrap=WORD)
		self.text.pack(anchor=W)
		self.openButton=Button(master=self.window,
								text="Open File",
								command=self.open)
		self.openButton.pack(side=LEFT)
		self.decipherButton=Button(master=self.window,
								text="Decipher Text",
								command=self.decipher)
		self.decipherButton.pack(side=LEFT)
		self.img = Image.open("../Original Python-Programme/kap_30/Thailand_2.png")
		w, h = self.img.size
		self.imgTk = ImageTk.PhotoImage(self.img)
		self.label.config(image=self.imgTk, width=w, height=h)
		self.window.mainloop()  

	def open(self):
		filename = filedialog.askopenfilename()
		if filename:
			self.img=Image.open(filename)
			self.imgTk = ImageTk.PhotoImage(self.img)
			self.label.config(image=self.imgTk)

	def decipher(self):
		a = np.array(self.img)	# read image to numpy array
		b = a[:,:,1]			# pick green channel
								# get reference green channel
		code=np.array(Image.open("../Original Python-Programme/kap_30/Thailand_2.png"))[:,:,1].clip(max=215)
		b -= code				# subtract reference
		#print("Code:", code)
		#print("B:", b[0,:])
		self.text.insert(END, "Decoded message:\n")
		self.text.insert(END, ''.join(self.decode(b.flatten().tolist()))+"\n")

	def decode(self, numbers):
		text = []
		for dig in numbers:
			try:
				if(LETTERS[dig] != ' ' or text[-1] != ' '):
					text.append(LETTERS[dig])
				else:
					continue
			except:
				text.append(' ')
		if(text[-1] == ' '):
			del(text[-1])
		#print(numbers[0:20])
		#print(text[0:20])
		return text

App()





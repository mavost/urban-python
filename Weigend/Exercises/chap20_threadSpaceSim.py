#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap20_threadSpaceSim.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 05/12/2017
#------------------------------------------------------------
''' Python 3 main - An example of using threads as inherited classes within tkinter lib
	-save tkinter code as *.pyw to supress console window
	
	https://pymotw.com/2/threading/

'''

from tkinter import Tk, Canvas, PhotoImage
from threading import Thread, Event
from time import sleep
from random import randint, choice
from PIL import Image, ImageTk						# try rotation next?

# logging output
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)


##############################################################################

class SpaceSim(object):						#
	def __init__(self):
		self.win = Tk()
		self.win.title('Space-Simulator - press q to exit')
		self.canvas = Canvas(master=self.win, width='10c',
								height='7c', bg='black')
		self.canvas.pack()
		m1 = PhotoImage(file='data/metgross.gif')
		m2 = PhotoImage(file='data/metklein.gif')
		o1 = PhotoImage(file='data/portal.gif')
		obs = [m1, m2, o1]
		self.spobjects = []
		
		for a in range(15):								#create 15 objects of random shape and add Threads to list
			img=choice(obs)
			#img=m1 if randint(1, 2)==1 else m2
			id_nr = self.canvas.create_image(50, -50, image=img)
			m=SpaceObject(canvas=self.canvas, id_nr=id_nr)
			self.spobjects.append(m)
		self.win.bind('<KeyPress-q>', self.close)
		self.win.bind('<KeyPress-q>', self.close)
		# for a in self.canvas.find_all():				#debug
			# print(a)
		self.win.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.win.mainloop()

	def on_closing(self):								#protocol handler
		for m in self.spobjects:
			m.stop()
			sleep(0.05)									#give threads time to close gracefully
		self.win.destroy()								#destroy GUI

	def close(self, event):
		for m in self.spobjects:
			m.stop()
			sleep(0.05)									#give threads time to close gracefully
		self.win.destroy()								#destroy GUI
	

##############################################################################

class SpaceObject(Thread):					# inherited Thread class, defining stuff to do in run()
											# 	and calling start() on the instance will internally
											# 	invoke run()
	
	def __init__(self, canvas=None, bild=None, id_nr=0):		# send ThreadID along
		super(SpaceObject, self).__init__()
		#Thread.__init__(self)
		self.c = canvas
		self.id = id_nr
		self._stop_event = Event()
		self.__restart()
		self.start()

	def stop(self):
		self._stop_event.set()

	def stopped(self):
		return self._stop_event.is_set()

	def __restart(self):
		self.x = randint(0, 250)
		self.y = randint(30, 100)
		self.vx = randint(-2, +2)
		self.vy = randint(1, 3)

	def run(self):
		logging.debug('running')
		while not self.stopped():
			sleep(0.05)
			self.x += self.vx
			self.y += self.vy
			self.c.coords(self.id, self.x, self.y)
			if self.y > 300:
				self.__restart()

##############################################################################		
sim=SpaceSim()
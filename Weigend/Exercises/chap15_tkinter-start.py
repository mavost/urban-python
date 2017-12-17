#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap15_tkinter-start.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 30/11/2017
#------------------------------------------------------------
''' Python 3 main - Testing the tkinter lib
	-save tkinter code as *.pyw to supress console window
'''

from tkinter import *
from time import sleep

def greeting():
	window.label.config(text='Hello!')

def farewell():
	window.label.config(text='Goodbye!')
	#needs threads
	#sleep(5)
	#window.label.config(text='A polite window')

#class Tk
window=Tk()
window.title('Demonstration')						#window title
window.geometry('500x600')							#window size


#class Label
window.label = Label(master=window,
					text='A polite window')
window.label.pack()

window.frame = Frame(master=window,
					relief=RIDGE, bd=2)
window.frame.pack()

#class Button					
window.button1 = Button(master=window.frame,
					text='Say Hello',
					command=greeting,
					width=20)
window.button1.pack()

window.button = Button(master=window.frame,
					command=greeting,				#method name without brackets
					borderwidth=2,					#alias: bd
					background='grey60',			#alias: bg, http://www.science.smith.edu/dftwiki/images/thumb/3/3d/TkInterColorCharts.png/
													#	or '#rgb' in 8bit hex or '#rrggbb' in 16bit hex
					foreground='#b27c47',			#alias: fg
					text='Say Nothing',
					font=('Times',20,'bold'),		#Tuple (family, size, [style]), http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/fonts.html
													#	common families: Arial, Courier, Comic Sans MS, MS Sans Serif, Symbol, System, Times, Verdana
													#	styles: bold, italic, underline, overstrike
					justify=LEFT,					#LEFT, RIGHT, CENTER
					underline=1,					#Tooltips letter highlighting
					width=20,						#size depending on text-based(row-size) or non-text-based(pixel-size) features of widgets
					height=2,						#size depending on text-based(row-size) or non-text-based(pixel-size) features of widgets
					relief=RIDGE,					#SUNKEN, RAISED, GROOVE, RIDGE, FLAT
					padx=2,
					pady=2)
					

window.button.pack()


window.button2 = Button(master=window.frame,
					text='Say Goodbye',
					command=farewell,
					width=20)
window.button2.pack()

frametypes=[SUNKEN, RAISED, GROOVE, RIDGE, FLAT]
for framecount in frametypes:
	label=Label(master=window, text=str(framecount),
			font=('Arial',10), bd=4, relief=framecount, padx=10)
	label.pack()
	
#shared event handler methods
#window.button.after(5000, greeting())						#after(ms, f[,arg[,...]]) still needs threads
#window.button.bell()										#warning sound
#window.button.bind(sequence=event, func=f[aaa])			#bind function to event
#window.button.bind_all(sequence=event, func=f[aaa])		#bind function to all widgets
#window.button.bind_class(className, sequence=event, func=f[aaa])			#bind function to one widget class
#window.button.cget(option)									#return current value of option
#window.button.configure(option=value,...)					#set new value to option(s)
#window.button.config(option=value,...)						#set new value to option(s)
#window.button.destroy()									#kill widget and child hierarchy
#window.button.option_clear()								#set widget options to default

window.name = Entry(master=window.frame)
window.name.pack()

################Radio Buttons
pill=IntVar()
RBMODES = [
        ('Red Pill', 1),
        ('Blue Pill', 2),
		('Purple Pill', 3),
    ]

def showrb():
	print(str(pill.get()))

for MODE in RBMODES:
	rb=Radiobutton(master=window.frame, text=MODE[0], value=MODE[1], 
		variable=pill, command=showrb)
	rb.pack(anchor='w',padx=150)
	if(MODE[1]==2): rb.select()


################Check Buttons
# vars=[]
# for var in range(3):
	# vars.append(StringVar())
	# vars[-1].set('0')

color1,color2,color3=StringVar(),StringVar(),StringVar()
for var in [color1,color2,color3]:
	var.set('0')

CMODES = [
        ('Red', 'r', '0'),
        ('Green', 'g', '0'),
		('Blue', 'b', '0'),
    ]
def mix():
	out=''
#	for var in vars:
	for var in [color1,color2,color3]:
		out+=var.get()
	print(out)
	
for MODE,var in zip(CMODES,[color1,color2,color3]):
	cb=Checkbutton(master=window.frame, text=MODE[0], onvalue=MODE[1], offvalue=MODE[2], variable=var, command=mix)
	cb.pack(anchor='w',padx=150)
	#if(MODE[1]==2): cb.select()

################Scaler
def rescale(event):
	window.scal_label.config(font=('Arial',window.scaler.get(),'bold'))
	
window.scaler=Scale(master=window, from_=5, to=80, length=350,
				command=rescale)
window.scaler.set(20)
window.scal_label=Label(master=window,
					text='X',font=('Arial',window.scaler.get(),'bold'))
window.scal_label.pack()
window.scaler.pack()


#Button(master=window, text='Quit', command=window.quit).pack(anchor='e', padx=150)
window.mainloop()

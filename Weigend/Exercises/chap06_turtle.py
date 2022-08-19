#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap06_turtle.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 10/10/2017
#------------------------------------------------------------
''' Python 3 main - a small piece of code
'''

from turtle import*

def baum(x):
	if x<5 :
		return
	else:
		forward(x)
		left(45)
		baum(x/2)
		right(90)
		baum(x/2)
		left(45)
		back(x)
	return

def round_t(rad=100,	#radius of the circle
			step=10     #reduction of the radius
			):
	""" this function draws a circle
	
	Two parameters
	Recursive call
	MvS 10.10.2017
	"""
	right(90)
	circle(rad)
	penup()
	left(90)
	forward(step)
	pendown()
	rad-=step
	
	if rad<10:
		return
	else:
		round_t(rad,step)
		return
	



def main():
	clear()
	showturtle()
	speed(5)
	forward(100)
	#round_t()
	#back(200)
	#round_t()
	baum(100)
	hideturtle()
	
	
	
main()

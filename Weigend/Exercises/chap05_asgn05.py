#Python3,mvs, 2017-09-27
#Chapter 5 / Assignment 5
import math
import random

z=random.randint(0,100)
guess=-1
while z!=guess:
    guess=int(input("Wie lautet meine Zufallszahl?:"))
    if guess < z:
        print("Zahl zu niedrig")
    elif guess > z:
        print("Zahl zu hoch")
    else:
        print("Zahl gefunden!")

print("Ende des Programms") 

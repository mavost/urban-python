#Python3,mvs, 2017-09-27
#Chapter 5 / Assignment 5 / Alternative solution using recursion
import math
import random

z=random.randint(0,100)

def verify_number(low,high,sol):
    guess=int(input("Wie lautet meine Zufallszahl?:"))
    if guess < sol:
        low=guess if guess>low else low
        print("Zahl zu niedrig - Bereich: "+str(low) +" - "+str(high))
        verify_number(low,high,sol)
    elif guess > sol:
        high=guess if guess<high else high
        print("Zahl zu hoch - Bereich: "+str(low) +" - "+str(high))
        verify_number(low,high,sol)
    else:
        print("Zahl gefunden!")
    return

verify_number(0,100,z)

print("Ende des Programms") 

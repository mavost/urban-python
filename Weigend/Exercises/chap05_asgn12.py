#Python3,mvs, 2017-09-27
#Chapter 5 / Assignment 12 / Multiplication Coaching

import time
from random import randrange
start = time.time()

for i in range(1,6):
    ran_A=randrange(2,21)
    ran_B=randrange(2,21)
    j=False
    while not j:
        result_in=int(input(str(ran_A)+" * "+str(ran_B)+" = "))
        if result_in == ran_A*ran_B:
            j=True
            print("CORRECT")
        else:
            print("TRY AGAIN")
        #j = False if result_in == ran_A*ran_B else True

end = time.time()

print("It took you %i seconds to solve the challenge." % (end-start))
print("Ende des Programms") 

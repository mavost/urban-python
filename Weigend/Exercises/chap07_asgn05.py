#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap07_asgn05.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 11/10/2017
#------------------------------------------------------------
''' Python 3 main - dancing partners - permutations
'''

males=set('m'+str(t) for t in range(1,5))
females=set('f'+str(t) for t in range(1,5))
teacher=set('t')
print(males,females,teacher)
pairs=[(a,b) for a in males | teacher for b in females | teacher if a!=b]
print()
print("Number of pairs: ", len(pairs))
print(pairs)
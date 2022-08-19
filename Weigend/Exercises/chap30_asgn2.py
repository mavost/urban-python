#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap30_asgn2.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 23/10/2017
#------------------------------------------------------------
''' Python 3 main - roll dice and histogram
'''
#pip install numpy-1.13.3+mkl-cp36-cp36m-win32.whl
#pip install get scipy-0.19.1-cp36-cp36m-win32.whl
import numpy as np
import matplotlib.pyplot as plt


a=np.random.randint(1,7,(100,2))
print(a)
b=np.sum(a,axis=1)
histo, bins = np.histogram(b, bins=11, range=(1.5,12.5))
plt.bar(bins[:-1]+.5, histo, align='center', facecolor='blue', alpha=0.33, width=1, edgecolor='black')

plt.xlabel('Eyes rolled')
plt.ylabel('Samples')
plt.title("Histogram of rolling two dice one hundred times")
plt.show()
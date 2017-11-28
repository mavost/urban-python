#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap30_matplotlib-in-numpy.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 19/10/2017
#------------------------------------------------------------
''' Python 3 main - example for plotting of numpy data
'''
import numpy as np
import matplotlib.pyplot as plt
# Draw axis
x=np.linspace(0,4*np.pi,130)
y=np.sin(x)

plt.plot(x, y, linewidth=2, color='r')
plt.axis('tight')
plt.show()


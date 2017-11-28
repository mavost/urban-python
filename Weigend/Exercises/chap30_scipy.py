#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap30_scipy.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 23/10/2017
#------------------------------------------------------------
''' Python 3 main - experiments with scipy
'''
#pip install numpy-1.13.3+mkl-cp36-cp36m-win32.whl
#pip install get scipy-0.19.1-cp36-cp36m-win32.whl
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def f(x):
	return x*x

print(integrate.quad(f, 0, 1))

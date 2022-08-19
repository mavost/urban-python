#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: 01_tutorial.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 27/10/2017
#------------------------------------------------------------
''' Python 3 main - scikit-learn intro
'''

from sklearn import datasets

iris = datasets.load_iris()
digits = datasets.load_digits()
#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap30_asgn3.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 23/10/2017
#------------------------------------------------------------
''' Python 3 main - load weather data
'''
import numpy as np
import matplotlib.pyplot as plt

wtbl = np.loadtxt("../Original Python-Programme/kap_30/dmd2_17_07_2016.csv", delimiter=";")
#print(wtbl)

plt.figure()
plt.subplot(1,2,1)
plt.plot(wtbl[:,1].transpose())
plt.title("Carbonmonoxide (NO) in Air")
plt.xlabel("time [h]")
plt.ylabel("concentration [µg/m³]")
plt.subplot(1,2,2)
plt.plot(wtbl[:,2].transpose())
plt.title("Carbondioxide (NO2) in Air")
plt.xlabel("time [h]")
plt.show()
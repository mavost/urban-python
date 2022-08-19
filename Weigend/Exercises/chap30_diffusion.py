#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap30_diffusion.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 20/10/2017
#------------------------------------------------------------
''' Python 3 main - diffusion project
'''
import numpy as np
import matplotlib.pyplot as plt

n_particles=200 #elements
t_max=100		#legth of simulated time

#create x_axis
t=np.arange(t_max)
#create array of all random movements for all elements in the range -1,0,+1
steps=2*np.random.randint(0,2,
						 (n_particles,t_max))-1
positions=np.cumsum(steps, axis=1)
sq_d=positions**2
mean_sq_d=np.mean(sq_d,axis=0)

# Draw
plt.figure()
plt.plot(t,np.sqrt(mean_sq_d), "b.",np.sqrt(t), "r-")
plt.xlabel("Time")
plt.ylabel("Mean Displacement")
plt.legend(("Simulation", "Theory"), loc=(0.6, 0.1))
plt.show()


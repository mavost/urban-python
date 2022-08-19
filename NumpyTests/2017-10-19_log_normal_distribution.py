#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: 2017-10-19_log_normal_distribution.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 19/10/2017
#------------------------------------------------------------
''' Python 3 main - example for lognormal distribution in numpy
'''
import numpy as np
import matplotlib.pyplot as plt
# Draw samples from the distribution
mu, sigma = 3., 1. # mean and standard deviation
s = np.random.lognormal(mu, sigma, 1000) #generate lognormal data

#Display the histogram of the samples, along with the probability density function:
count, bins, ignored = plt.hist(s, 100, normed=True, align='mid')

x = np.linspace(min(bins), max(bins), 10000)
pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))/
		(x * sigma * np.sqrt(2 * np.pi)))

plt.plot(x, pdf, linewidth=2, color='r')
plt.axis('tight')
plt.show()


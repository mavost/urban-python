#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: 2017-10-19_Amdahls_Law.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 19/10/2017
#------------------------------------------------------------
''' Python 3 main - implement Amdahl's Law using numpy
'''
import numpy as np

#a programm consists of fractional elements with a maximal speedup achived by parellization through additional hardware
data_in=np.ones((1,2))
entry_f=0
entry_s=0
#generate a list of sub-process and speed up
while True:
	try:
		entry_f=float(input("Please enter fraction of process time [%] or (q) to proceed:"))
	except (ValueError,TypeError):
		print("Entry complete.")
		break
	try:
		entry_s=float(input("Please enter max_speedup(f) [float, def=1.0]:"))
	except (ValueError,TypeError):
		print("...using default.")
		entry_s=1.0
	data_in=np.append(data_in,[[entry_f,entry_s]],axis=0)
#remove last element if there was input
if data_in.shape[0]>1:
	data_in=data_in[1:]

#data_in=np.array([[11,18,23,48],[1,5,20,1.6]]).T
data_calc=data_in.copy()
print("f [%]:\t s [float]")
data_calc[:,0]/=100.0
max_rate=float(1/sum(data_calc[:,0]/data_calc[:,1]))
print(data_calc)
print("Max Achievable Speedup:")
print("%8.2f" % max_rate)

'''for upgrading the compute environment with an increasing
number of core pairs to the effective maximum calculate the speed up
and the fractional acceleration'''
scal=np.ones(data_calc.shape)
res=np.ones((1,3))
for a in range(2,int(2*(data_calc.max(axis=0)[1]//2+1))+1,2):
	scal.fill(a)
	scal[:,0]=2
	#make sure that core boost is truncated by speedup limit of each element in the process
	trial=np.where(scal>data_calc,data_calc,scal)
	#print(trial)
	rate=float(1/sum(trial[:,0]/trial[:,1]))
	res=np.append(res,[[a,rate,100.0*rate/max_rate]],axis=0)
print("#cores [int]:\t s_calc [float]")
print(res)
#subjectively identify an effective hardware upgrade 
for a in res:
	if a[2]<95 :
		continue
	else :
		print("Optimum number of cores: ", a[0])
		break

#plot result
import matplotlib.pyplot as plt
plt.plot(res[:,0], res[:,1], linewidth=2, color='r')
plt.axis('tight')
plt.show()


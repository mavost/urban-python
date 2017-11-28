#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap30_clouds.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 23/10/2017
#------------------------------------------------------------
''' Python 3 main - calculate cloud coverage
'''

import numpy as np
import matplotlib.pyplot as plt

#pip install pillow
import PIL

#get the path to data right
import os
DATA_in = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/cirrus-cloud.png'))
DATA_out = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/cirrus-cloud_mask.png'))



#load RGB image
img=np.array(PIL.Image.open(DATA_in))
#get blue channel from image divided by mean of all channels
img_blue=img[:,:,2]/np.mean(img, axis=2)


abin_size=64
#generate histogram of three channels
#rn, rbins, rpatches = plt.hist(img[:,:,0], bin_size, normed=0, facecolor='red', alpha=0.33)
#gn, gbins, gpatches = plt.hist(img[:,:,1], bin_size, normed=0, facecolor='green', alpha=0.33)
#bn, bbins, bpatches = plt.hist(img[:,:,2], bin_size, normed=0, facecolor='blue', alpha=0.33)
rn, r_bins = np.histogram(img[:,:,0], bins=abin_size, range=(0,255), density=True)
awidth=float(np.diff(r_bins)[0])
plt.bar(r_bins[:-1], 100*awidth*rn, align='center', facecolor='red', alpha=0.33, width=awidth)
gn, g_bins = np.histogram(img[:,:,1], bins=abin_size, range=(0,255), density=True)
plt.bar(g_bins[:-1], 100*awidth*gn, align='center', facecolor='green', alpha=0.33, width=awidth)
bn, b_bins = np.histogram(img[:,:,2], bins=abin_size, range=(0,255), density=True)
plt.bar(b_bins[:-1], 100*awidth*bn, align='center', facecolor='blue', alpha=0.33 , width=awidth)

plt.xlabel('Color intensity')
plt.ylabel('Percentage')
plt.title("Histogram of all raw channels")
plt.legend(('Red','Green','Blue'))
plt.show()


#====================================================
bin_size=128
hist, bin_edges = np.histogram(img_blue[::10,::10], bins=bin_size, density=True)
#print(hist, bin_edges)
hist_width=float(np.diff(bin_edges)[0])

#plot histogram in bar chart
# plt.bar(bin_edges[:-1], hist*100*hist_width, align='center', alpha=0.5, width=0.9*hist_width)
# plt.title("Histogram of normalized blue channel")
# plt.show()

#run a smoothing operation
N=5 #kernel width
smooth_hist=np.convolve(hist, np.ones((N,))/N, mode='same')

#plot histogram in bar chart
plt.bar(bin_edges[:-1], smooth_hist*100*hist_width, align='center', alpha=0.5, width=0.9*hist_width)
plt.title("Histogram of smoothed normalized blue channel")
plt.show()


# Draw greyscale image of blue channel
plt.imshow(img_blue, cmap=plt.cm.gray)
plt.colorbar()
plt.show()


#define cutoff as max in smooth histogram
cut_off=bin_edges[smooth_hist.argmax()]+N*hist_width
max_val=img_blue.max()
print("cut_off: %5.2f and max_val: %5.2f" % (cut_off, max_val))

# Draw mask and calculate ratio of black/all pixels in cloud mask
#cut_off=1.08
#img_mask=img_blue>cut_off
img_mask=img_blue.clip(cut_off,max_val)
img_mask= 1*(1-1/(max_val-cut_off)*(img_mask-cut_off))

plt.imshow(img_mask, cmap=plt.cm.gray)
plt.colorbar()
plt.show()
print("Cloud coverage in image using a cut-off of %5.2f is at: %5.1f percent" %
		(cut_off,100.0*(1-np.mean(img_mask))))

#multiply inverse mask with alpha_channel to enable full transparency
img_mask=img_mask
img_mask*=255
#img[:,:,3]*=np.logical_not(img_mask)
img[:,:,3]=img_mask.astype('uint8')

#export masked image
result = PIL.Image.fromarray(img)
result.save(DATA_out)

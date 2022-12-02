import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm

# change the current directory to my workshop directory
workshop_dir = '/Users/meifeng/Dropbox/BNL/CSC/Mini-Semester-Jan2015/examples/'
os.chdir(workshop_dir)

# input file
infile = 'ran_data.dat'

# read and unpack the data
x, y = np.loadtxt(infile, unpack=True)
nbins = 100

# fit the data to the normal distribution 
# and obtain the mean and standard deviation
(mu, sigma) = norm.fit(y)

print "From Gaussian fit, mu = ", mu, "sigma = ", sigma

fig = plt.figure()

# position of the subplots. The numbers read as M x N plots, ith plot
timeseries = fig.add_subplot(211)
histogram = fig.add_subplot(223)
histogram_norm = fig.add_subplot(224)

# make the histogram plots!
histogram.hist(y, nbins, normed=False, align='mid', 
    facecolor='blue', alpha=0.9)
histogram.set_xlabel('Random Number Value')
histogram.set_ylabel('Counts')
n, bins, patches = histogram_norm.hist(y, nbins, normed=True, 
    align='mid',facecolor='green', alpha=0.9)

histogram_norm.set_xlabel('Random Number Value')
histogram_norm.set_ylabel('Fraction')

# plot the Gaussian fit
gauss = mlab.normpdf(bins, mu, sigma)
histogram_norm.plot(bins, gauss, 'r-', linewidth=2)

# time series plot
timeseries.plot(x,y,'r-')
timeseries.set_xlabel('Index')
timeseries.set_ylabel('Random Number Value')
fig.subplots_adjust(hspace=0.5,wspace=0.5)

# display the plot
fig.show()

# save a hard copy
fig.savefig('histogram.pdf')

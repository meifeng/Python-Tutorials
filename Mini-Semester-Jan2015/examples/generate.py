import os
import random
import matplotlib.pyplot as plt

# change the current directory to my workshop directory
workshop_dir = '/Users/meifeng/Dropbox/BNL/CSC/Mini-Semester-Jan2015/examples/'
os.chdir(workshop_dir)

# set the number of random numbers we want
N = 100

# mean 
mu = 0.0

# standard deviation
sigma = 1.0

# create an empty list
data = []

# append each random number to the list
for i in range(N):
    print i, N
    data.append(random.gauss(0,1.0))
    
plt.plot(range(N),data)
plt.show()

# open the output file to write
outfile = open('ran_data.dat','w')

# write the data to disk
for i in range(N):
    outfile.write("%d %e\n" %(i, data[i]))

outfile.close()



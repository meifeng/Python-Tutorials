import os
from math import sqrt
import matplotlib.pyplot as plt

# create a function to calculate the mean and standard deviation 
# of an input list
def stat(data):
    N = len(data)
    sum = 0.0

    for i in range(N):
        sum += data[i]
    avg = tot/N

    sum2 = 0.0
    for i in range(N):
        sum2 += (data[i] - avg)**2
        var = sum2/N
    return avg, sqrt(var)
   
# change the current directory to my workshop directory
workshop_dir = '/Users/meifeng/Dropbox/BNL/CSC/Mini-Semester-Jan2015/examples/'
os.chdir(workshop_dir)

data = []

infile = open('ran_data.dat','r')
for line in infile: # line is a string
    _, val = line.split() # _ is a dummy variable
    data.append(float(val)) # needs to convert string to float
infile.close()

N = len(data)
sum = 0.0
    
for i in range(N):
    sum += data[i]
avg = sum/N

sum2 = 0.0
for i in range(__):
    sum2 __ (data[i] - avg)**2
var = __/N





(average, error) = stat(data)


print 'average, standard deviation = ', stat(data)
plt.plot(data,'r-o')
plt.axhline(y=average,color='b')
plt.axhline(y=average+error,color='g')
plt.axhline(y=average-error,color='g')

plt.show()

import random
import math

#user-defined function to calculate the mean of a list
def mymean(x_in):
    N = len(x_in)
    total = 0.0
    for i in range(N):
        total = total + x_in[i]
    return total/N

#user-defined function to calculate the standard deviation of a list
def mystdev(x_in):
    N = len(x_in)
    total = 0.0
    mean = mymean(x_in)
    for i in range(N):
        total = total + (x_in[i] - mean)**2
    return math.sqrt(total/N)


#create an empty list
data = [] 
N = 10000

for i in range(N): 
    #generate a random number and add it to the data list
    data.append(random.random())

mean = mymean(data)
stdev = mystdev(data)

print "The mean and standard deviation of ", N, "random numbers are:", mean, stdev

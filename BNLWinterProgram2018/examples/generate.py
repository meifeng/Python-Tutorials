import os
import random
import matplotlib.pyplot as plt
from math import sqrt

N = 10000
mu = 0.0
sigma = 1.0
data = []
random.seed(1234)
for i in range(N):
    rnum=random.gauss(0,1.0)
    print i, rnum
    data.append(rnum)
    
plt.plot(range(N),data)
plt.show()

def stat(data):
    tot = 0.0
    num_data = len(data)
    for i in range(num_data):
        tot += data[i]
    avg = tot/num_data
    
    for i in range(num_data):
        tot += (data[i] - avg)**2
        var = tot/num_data
    return avg, sqrt(var)
   
calc_mu, calc_sigma=stat(data)
print calc_mu, calc_sigma


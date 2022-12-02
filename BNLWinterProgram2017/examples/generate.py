import os
import random
import matplotlib.pyplot as plt
from math import sqrt

N = 10
mu = 0.0
sigma = 1.0
data = []
random.seed(1234)
for i in range(N):
    rnum=random.gauss(mu,sigma)
    print i, rnum
    data.append(rnum)
    
plt.plot(range(N),data)
plt.show()

def stat(_data):
    tot = 0.0
    num_data = len(_data)
    for i in range(num_data):
        tot = tot + _data[i]
    avg = tot/num_data
    
    for i in range(num_data):
        tot += (_data[i] - avg)**2
        var = tot/num_data
    return avg, sqrt(var)
   
calc_mu, calc_sigma=stat(data)
print calc_mu, calc_sigma


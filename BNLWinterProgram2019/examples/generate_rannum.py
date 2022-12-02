import random
import matplotlib.pyplot as plt

flat_dist=[]
gauss_dist=[]
N = 10**5
histbins=50
plt.clf()

for i in range(N):
    flat_dist.append(random.random())
    gauss_dist.append(random.gauss(0,1.0))
fig = plt.figure()

gauss_hist = fig.add_subplot(211)
flat_hist = fig.add_subplot(212) 
gauss_hist.hist(gauss_dist,histbins)

flat_hist.hist(flat_dist,histbins)
plt.show()
    
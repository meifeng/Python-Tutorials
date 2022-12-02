#a Python program to calculate the value of pi 
#using Monte Carlo methods

from math import sqrt
from random import random

N = 10**7

Ninside = 0

for i in range(N):
    x = random()
    y = random()
    if sqrt(x**2+y**2) < 1.0:
        Ninside = Ninside + 1

print "pi is approximately ", 4.0 * Ninside / N


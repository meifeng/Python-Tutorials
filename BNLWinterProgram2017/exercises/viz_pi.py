# a Python program to estimate the value of pi by Monte Carlo methods
# with visualization

from random import random, seed
from math import sqrt
from PIL import Image
from PIL import ImageDraw

TRIALS=10**7
XMAX=500
YMAX=500

def main():
    #seed(6666)
    inside = 0
    img = Image.new('RGB', (XMAX, YMAX), "white")
    draw = ImageDraw.Draw(img)
    draw.arc([0,XMAX,YMAX,0], 0, 90, fill="black")
    for i in xrange(TRIALS):
        x = random()
        y = random()
        if sqrt(x**2+y**2) < 1:
            inside +=1
            draw.point((int(x*XMAX), int(y*YMAX)), fill="blue")
        else:
            draw.point((int(x*XMAX), int(y*YMAX)), fill="red")
    img.save('pi.png')
    img.show()
    print 'With ', TRIALS, 'samples'
    print 'Estimated pi is: ', 4.0 * inside / TRIALS

if __name__ == '__main__':
    main()

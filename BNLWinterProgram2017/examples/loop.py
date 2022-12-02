print "for loop:"
for n in range(10):
    print n
    
for n in range(10):
    if n%2 == 0:
        print n, "is an even number"
    else:
        print n, "is an odd number"
        
print "while loop:"        
x = 11
while x < 20:
    if x%2 == 0:
        print x, "is an even number"
    else:
        print x, "is an odd number"
    x=x+1
    
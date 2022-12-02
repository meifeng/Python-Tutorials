print "Type a number:"
n = input()

if type(n) == int:
    if n%2 == 0:
        print n, "is an even number"
    else:
        print n, "is an odd number"
else:
    print n, "is not an integer"
    

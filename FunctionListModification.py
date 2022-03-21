def chop(a):
    del a[0]
    del a[len(a) - 1]

def middle (a):
    print a[1:len(a)-1]

print 'Uses the chop function'
Dlist = [10, 20, 13, 33, 45]
chop (Dlist)
print Dlist

print
print 'Uses the middle function'
Dlist = [10, 20, 13, 33, 45]
middle (Dlist)

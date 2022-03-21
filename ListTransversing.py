##print 'Transversing the items of a list backward movement'
##a = [10, 21, 11, 34]
##index = len(a) - 1
##while index > -1:
##	print a[index]
##	index = index - 1
##print 'Done'
##
##print
##print 'Transversing the items of a list forward movement'
##a = [10, 21, 11, 34]
##for item in a:
##    print item
##print 'Done'

print
print 'Changing the order of a list'
a = [10, 21, 11, 34]
b = [10, 21, 11, 34]
count = 1
print a
for i in range(len(a)/2):
    a[i] = a[i-count]
    a[i-count] = b[i]
    #a[count] = b[count-i]
    #a[len(a)] = a[i]
    count = count - 2
    #a[count] = b[i-1]
    print a
print 'Done'

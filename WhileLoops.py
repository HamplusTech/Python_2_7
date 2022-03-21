n = 5
while n > 0:
    print n
    n = n-1
print 'Blastoff!'

##print 'An infinite loop'
##n = 10
##while True:
##    print n,
##    n = n - 1
##print 'Done!'

while True:
    line = raw_input('> ')
    if line == 'done':
        break
    print line
print 'Done!'

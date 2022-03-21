print 'To end this program, type (done)'
total = 0
count = 0
average = 0
print ">>> type numeral(s) only\n"
while True:
    raw = raw_input (">>> ")
    try:
        if raw == 'done':
            break
        else:
           total = total + float (raw)
           count = count + 1
           average = total / count
    except:
        print 'Invalid input'
print 'total' , 'count' , 'average'
print total , count , average

print 'A loop sample to find the largest number in a list'
largest = None
print 'Before:', largest
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print 'Loop:', itervar, largest
print 'Largest:', largest

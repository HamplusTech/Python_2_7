print 'To end this program, type (done)'
total = 0
count = 0
average = 0
largest = None
smallest = None
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
           if smallest is None or float(raw) < smallest:
               smallest = float (raw)
           if largest is None or float(raw) > largest:
                largest = float (raw)
    except:
        print 'Invalid input'
print 'total' , 'count' , 'average' , 'smallest' , 'largest'
print total , count , average , smallest , largest

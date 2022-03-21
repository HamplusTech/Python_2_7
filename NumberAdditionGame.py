total = 0; smallest = None
count = 0; largest = 0
avg = 0
while True:
    a = raw_input('Enter a number ')
    try:
        if a == 'done':
            break
        else:
            a = int(a)
            total = total + a
            count = count + 1
            avg = float(total / count)
            if smallest is None or smallest > a:
                smallest = a
            if largest == 0 or largest < a:
                largest = a
    except:
        print 'bad data'
        continue
print 'total', 'count', 'avg'
print total, count, avg
print 'largest', 'smallest'
print largest, smallest
            

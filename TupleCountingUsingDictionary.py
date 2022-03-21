fname = 'mbox.txt'
try:
    fhand = open(fname)
except:
    print ('Error Opening File: ', fname)

count = dict()
times = 0
for lines in fhand:
    lines = lines.rstrip()
    if not lines.startswith('From'):continue
    if len(lines) == 0:continue
    words = lines.split()
    address = words[1]
    for address in words:
        if not address in count:
          count[address] = count.get(address, times + 1)
        else:
            count[address] = count.get(address, times + 1)
    print (count)
    

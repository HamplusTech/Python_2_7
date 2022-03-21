while True:
    line = raw_input('>>>')
    if line[0] =='#':
        continue
    if line == 'done':
        break
    print line
print 'DONE!!!'

n=10
while n>0:
    print n
    n=n-1
print 'DONE!'

while True:
    line = raw_input('>')
    if line=='done':
        break
    print line
print 'DONE!'

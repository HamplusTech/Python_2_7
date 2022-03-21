fname = 'mbox-0.txt'
try:
    fhand = open(fname)
except:
    print 'Error trying to open the file:', fname
count = 0
print 'File Processed ---', fname
for line in fhand:
    line = line.rstrip()
    if len(line) == 0:continue
    if not line.startswith('From '):continue
##    if not line.split()[0] == 'From':continue     #this is alternative to using startswith method
    count = count + 1
    words = line.split()
    answer = words[1]
    print answer
print "Total lines having 'From ' =",count 

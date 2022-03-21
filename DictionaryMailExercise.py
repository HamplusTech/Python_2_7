fname = 'mbox-0.txt'
try:
    fhand = open(fname)
except:
    print 'Error Opening File: ', fname

count = dict()
a = ''
aa = list()
for lines in fhand:
    lines = lines.strip()
    if not lines.startswith('From '):continue
    if len(lines) == 0: continue
    words = lines.split()
    day = words[2]
    a = a + ' '+ day
a = a.split()
for word in a:
    count[word] = count.get(word,0) + 1
print count


fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print 'Error Opening File: ', fname

count = dict()
a = ''
aa = list()
for lines in fhand:
    lines = lines.strip()
    if not lines.startswith('From '):continue
    if len(lines) == 0: continue
    words = lines.split()
    day = words[1]
    a = a + ' '+ day
a = a.split()
for word in a:
    count[word] = count.get(word,0) + 1
print count

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
    day = words[1]
    a = a + ' '+ day
a = a.split()
for word in a:
    count[word] = count.get(word,0) + 1

key_list = list()
aaa = count.values()
aaa_sorted = sorted(aaa)
aaa_max = max(aaa_sorted)
for key in count:
    if count[key] == aaa_max:
        print key, aaa_max


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
    email = words[1]
    email_split = email.split('@')
    domain_name = email_split[1]
    a = a + ' '+ domain_name
a = a.split()
for word in a:
    count[word] = count.get(word,0) + 1
print count

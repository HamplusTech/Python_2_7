# A list is like [a,s,d,f]
# A dictionary is like {'and': '', 'mind-numbing': ''}
# or like dict([('1','one'),('2','two')])
# A set is like ({('1','one'),('2','two')})

word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print d


word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print d


fname = raw_input('Please Enter File Name: ') # use remeo.txt as file name
try:
    fhand = open(fname)
except:
    print 'File Opening Error!', fname

count = dict()
for lines in fhand:
    words = lines.split()
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
print count

import string
fname = raw_input('Please Enter File Name: ') # use remeo - Copy.txt as file name
try:
    fhand = open(fname)
except:
    print 'File Opening Error!', fname

count = dict()
for lines in fhand:
    lines.translate(None, string.punctuation) #removes punctuations
    lines = lines.lower() #turns all to lowercase
    words = lines.split()
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
print count

fname = 'remeo - Copy.txt'
try:
    fhand = open(fname)
except:
    print 'Error Opening the file: ',fname

import string
word_dict = dict()
word_list = list()
for lines in fhand:
    if len(lines) == 0: continue
    lines = lines.translate(None, string.punctuation)
    lines = lines.lower()
    lines = lines.strip()
    words = lines.split()
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] +=1

for key, val in word_dict.items():
    word_list.append((val, key))

word_sort = list()
word_sort = sorted(word_list,reverse=True)

word_res = list()
for key, val in word_sort:
    word_res.append((val, key))
print tuple(word_res)

print 'The ten most common words are:'
for word, count in word_res[:10]:
    print word, '\t\t', count

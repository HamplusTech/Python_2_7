fname = 'words-0.txt'
try:
    fhand = open(fname)
except:
    print 'Error opening file'
words_dict = dict()
words_list = list()
for lines in fhand:
    lines = lines.rstrip()
    if lines.startswith(' '): continue
    if (lines) == '':continue
    #if len(lines) == 0: continue  # does the same thing as the above
    words = lines.split(' ')
    if len(words) == 0: continue
##    words = str(words)
##    words_dict[words] = ''
    words_list = words_list + words # makes the list to be one list
##    words_list.append(words) # makes the list to have sublists
##    print words_list
##words_list = str(words_list)
##words_dict[words_list] = ""

for word in words_list:
    words_dict[word] = ''
print words_dict
print 'to' in words_dict

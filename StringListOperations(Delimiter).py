##print 'A String to Characters'
##s = 'JohnPaul'
##s_list = list(s)
##print s, '\t', s_list
##
##print
##print 'A String to Words'
##y = 'I have a grade one loving habit for Ese'
##y_words = y.split()
##print y, '\t', y_words
##
##print
##print 'A string to Words Using Delimiter'
##u = 'I.Have.Known.Ese.For.Years'
##delimiter = '.'
##u_words = u.split(delimiter)
##print u, '\t', u_words
##
##print
##print 'Joining Strings and Replacing Delimiter'
##u = 'I.Have.Known.Ese.For.Years'
##delimiter = '.'
##u_words = u.split(delimiter)
##delimiter2 = ' '
##u_words_new = delimiter2.join(u_words)
##print u, '\n', u_words, '\n', u_words_new

print
print 'Parsing Lines (prints a particular word from a line)'
fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print "File can't be opened: ", fname
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print words[2]

print
print 'Another method'
fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print 'Error in opening file: ', fname
for lines in fhand:
    words = lines.split()
##    print 'Debug:', words     #Used to show debug info
    if len(words) == 0 or words[0] != 'From':continue
##    if words[0] != 'From':continue      #correct code
    print words[2]

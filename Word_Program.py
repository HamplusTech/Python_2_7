name = raw_input('Enter file:')
#it reads from "C:/Python27/"
#type words.txt
handle = open(name, 'r')
text = handle.read()
words = text.split()
counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print bigword, bigcount

print
print 'A simple demostration of while iteration'
n=5
while n>0:
    print n
    n=n-1
print 'end'

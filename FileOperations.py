fhand = open('Mbox.txt')
for line in fhand:
    lineNew = line.rstrip ()
    # Skip 'uninteresting lines'
    if not lineNew.startswith('From') :
        continue
    # Process our 'interesting' line
    print lineNew
    #print line

print 'To count number of lines'
a = open('Mbox.txt')
count = 0
for line in a:
    count = count + 1
print 'Line Count:', count

print 'To find total charaters in a file'
a = open('Mbox.txt')
char = a.read()
totchar = len(char)
print 'Total characters Count:', totchar

print 'To display the total content of a file as it is'
a = open('Mbox.txt')
char = a.read()
b = len(char)
b1 = int(b)
c = char[:b1]
print c

print 'prints lines that have @uct.ac.za'
fhand = open('Mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1 :
        continue
    print line

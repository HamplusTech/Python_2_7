print 'This extracts 0.8475 from X-DSPAM-Confidence: 0.8475 and converts to floating number'
string = 'X-DSPAM-Confidence: 0.8475'
a = string.find(':')
b = a + 1
b1 = b + 1
c = string[b1:]
d = float(c)
print a
print b
print b1
print c
print d

print 'A program that takes a string and replaces some characters with some and outputs the new string'
a = raw_input('Please enter a string\n')
b = raw_input('Please enter the numbers of character you want to cut counting from the first character as zero\n')
c = int(b)
d = a[:c+1]
e = a.strip(d)
f = raw_input('Enter the new characters\n')
g = a.replace(a,f) + e
print 'done'

print a
print b
print c
print d
print e
print f
print g

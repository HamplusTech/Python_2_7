data = 'banana'
count = 0
for char in data:
    if char=='a':
	    count=count+1
print count

print 'Counting Letter using function'

def count (word,letter):
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    return count

a = raw_input('Please enter the word\n')
b = raw_input('Please enter the letter you want to count\n')
print count(a,b)

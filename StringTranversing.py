print 'String Tranversing from first to last letter'
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print letter
    index = index + 1

print 'String Tranversing from last to first letter'
fruit = raw_input('Please enter input to transverse\n')
index = len(fruit) - 1
while index > -1:
    letter = fruit[index]
    print letter
    index = index - 1

print 'Transversing using for --- loop'
data = raw_input('Enter an input\n')
for i in data:
    print i
print 'Done'

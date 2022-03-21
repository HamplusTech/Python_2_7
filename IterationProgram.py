# A promgram that displays and sum the next ten numbers as well as the previous ten numbers
print 'Enter a number'
try:
    x = int(raw_input ())
    x2 = x
    x3 = x
    sumx2 = 0
    sumx3 = 0
    for i in [1,2,3,4,5,6,7,8,9,10]:
        x2 = x2 - 1
        sumx2 = sumx2 + x2
        print x2, sumx2
    for j in [1,2,3,4,5,6,7,8,9,10]:
        x3 = x3 + 1
        sumx3=sumx3 + x3
        print x3, sumx3
except:
    print 'Please enter a number only'

# A program that detects what was typed by the user [whether string or number]
print 'enter a number'
a = raw_input()
try:
    b = int(a)
except:
    b = a
if type(b) == int:
    print 'You have entered a number'
else:
    print 'You entered a string'

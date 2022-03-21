# A program to find the maximum of three numbers
a = raw_input('enter the first number: ')
b = raw_input('enter the second number: ')
c = raw_input ('enter the third number: ')
if a>b and a>c:
    print a, 'is greatest of', b , c
elif b>c and b>a:
    print b, 'is greatest of', a , c
elif c>b and c>a:
    print c, 'is greatest of', a , b
else:
    print ' non is greatest'

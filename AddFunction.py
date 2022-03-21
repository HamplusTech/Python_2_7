def Add (m,n):
    try:
        m = int(m)
        n = int(n)
        if type(m) == int and type(n) == int:
            total = m + n
            return total
    except:
        print 'pleease enter a numeric input'
    
print
# A program that takes two numbers and sum them
print 'A program that takes two numbers and sum them'
print 'input the first number'
a = raw_input()
print 'enter the second number'
b = raw_input()
c = Add(a,b)
print 'the sum of ' + str(a) + ' and ' + str(b) + ' is ' , c

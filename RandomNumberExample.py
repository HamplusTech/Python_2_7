import random
for i in range(10):
	x = random.random()
	print x

print
print 'values of an angle in differen trignometry measurement'
import math
x = 60
degree = x
radian = degree /360.0 * 2 * math.pi
print x, degree, radian
print 'sin, cos and tan of ', x
sine = math.sin(x)
cosine = math.cos(x)
tangent = math.tan(x)
print sine, cosine, tangent


print
print 'A game that ask for an input thrice from a user and outputs one randomly'
import random
x = raw_input('Please enter an input\n')
y = raw_input('Please enter an input\n')
z = raw_input('Please enter an input\n')
b = [x, y, z]
a = random.choice(b)
print 'One of your inputs as selected from random is ', a

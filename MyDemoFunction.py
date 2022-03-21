'''a  = 5
while a >= 0:
    y = a + 2
    print (y)
    break '''    # without this break it give the same value of y repeatedly
'''a  = 5
#for a in range(1,10):
while a <= 10:
    y = a + 2
    print (a, y)
    a = y + 0.5
    break  # with this break, it give the value of y = a + 0.5 for only a = 1'''
'''a  = 5
#for a in range(1,10):
while a <= 10:
    y = a + 2
    print (a, y)
    a = y + 0.5
    break  # without this break, it give all the values of y = a + 0.5 the range of a
'''
'''for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            #print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')'''

'''def FunctionDemo_1Arg(a):
    print(a)'''
'''def FunctionDemo_2Arg(a,arg2):
    b = a/4 + 2*arg2
    print(b)'''
'''def FunctionDemo_3Arg(a,arg2,c):
    print(a,arg2,c)'''
'''def sign_of_number(a):
    if a > 0.0:
        sign = 'positive'
    elif a < 0.0:
        sign = 'negative'
    else:
        sign = 'zero'
    return sign'''
'''for a in range(1, 10, 2):
    print (a)
else:
    print ('End of range')'''
'''t = 2
u = 4
a = 10
dt = 2   # define the incremental step for t
# Now we introduce the while loop to determine the range of t
while t <= 20:
    y = u*t + (1/2)*a*t**2
    print (y)
    t = t + dt'''
'''def Newton (u, t, dt):
    while t <= 20:
        y = u*t + 0.5*10*t**2
        print (y)
        t = t + dt'''



'''from numpy import*
from pylab import*
x= arange(10)
print x
plot(x)
show()'''
'''from pylab import*
L= [966e-9, 724e-9, 580e-9, 483e-9]
EW = [52504276.2619,26677316.0835,5466923.23763,1640758.63318]
ERJ = [1194900.36873, 5049224.40445, 15324170.5275, 38236811.7992]
EP =[5.62475222513,1.02166235521,4.05026780609,2.40278844437]
plot(L, EW, L,ERJ, L, EP)
xlabel('wavelength')
ylabel('Emissive power $E$')
show()
x0=11.31
y=1400
x1 = x0 + (1/3.0)*((1400/11**2)-x0)
print (x1)'''
'''n=1
a= 0.74 #Specific gravity
b = 12  # Proportionality of carbon
d= n*a*b*3.6667
print(d)'''

from numpy import*
from pylab import*
'''L = arange(2,10,2)
T = [2.84, 4.01, 4.92, 5.68, 6.35]
plot(L,T)
show()'''
x = arange(0, 40, 0.5)
#y = sin(x/3) - cos(x/5)
z = sin(x)
plot(x, z, 'o')
#plot(x,y, '0')
show()

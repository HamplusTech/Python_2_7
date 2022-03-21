def compute_pay (hour, rate):
    pay = float(hour) * float (rate)
    return pay

print "The Program Starts here!"
a = raw_input("Please enter hours worked\n")
b = raw_input("Please enter the rate per hour\n")
try:
    a = float(a)
    b = float(b)
##    if type(a) == float or type(b) == float:
    c = compute_pay(a,b)
    print "Your total pay is\n", c
##    else:
##        print "Please enter numbers as input"
except:
    print "Please enter numbers as input"

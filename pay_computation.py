def computepay(hour,rate):
    pay=hour*rate
    return pay

a = raw_input('Enter hour\n')
b = raw_input ('Enter rate\n')
computepay(a,b)
#################
# Pay Computation Program
hour = raw_input ('Enter the hours worked\n')
rate = raw_input ('Enter the rate of pay per hour\n')
try:
    if float(hour)>40:
        bonus = 1.5 *  float(rate) # * ((float(hour)-40)) 
        pay = float(hour) * float(rate) + bonus
    else:
        pay = float(hour) * float(rate)
    #pay = float(hour) * float(rate) + bonus
    print 'Your Total Pay is: ', pay
except:
    print ' Please enter a numeral'
print
print
print
print 'Designed By Hamplus Tech Intl.'

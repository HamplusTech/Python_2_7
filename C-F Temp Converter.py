# This program converts Temperature
converter = raw_input('Fahrenheit to Celsius type 1 otherwise type 2\n')
if converter == '1':
    FTemp = raw_input('Enter Fahrenheit Temperature: \n')
    try:
        Fah = float(FTemp)
        Cel =(Fah - 32.0) * 5.0/9.0
        print Cel, 'is the Celsius Temperature of ', Fah
    except:
        print 'please enter a number'
elif converter == '2':
    CTemp = raw_input ('Enter Celsius Temperature: \n')
    try:
        Cel = float(CTemp)
        Fah = ( Cel * 9 / 5 ) + 32.0
        print Fah, 'is the Fahrenheit Temperature of ', Cel
    except:
        print 'please enter a number'
else:
    print 'Wrong entering. Enter 1 or 2'
    

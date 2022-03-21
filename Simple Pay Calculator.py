#A program that calculates a workers pay from the hours spent
hour = int (raw_input ("Please Enter the Hours spent\n "))
rate = float (raw_input ("Please enter the rate per hour\n "))
Total_Pay = hour * rate
print 'Your total pay is ', str(Total_Pay) + ' .Thanks for your time and effort.'

#A program that calculates a workers pay from the hours spent and gives bonus
print 'enter the hours worked'
hours = raw_input()
rate = raw_input('Enter the rate for pay per hours\n ')
try:
    hours = int(hours)
    rate = int(rate)
    pay = hours * rate
    if hours > 40:
        bonus = 1.5 * pay
        tpay = pay + bonus
    else:
        tpay = pay
        bonus = 0
    print 'Your total pay is ', str(tpay) + '. You earned a bonus of ', str(bonus) + ' for working above 40 hours. Thanks'
except:
    print 'Please enter a number'

x = raw_input('Please enter a number\n ')
if x<5 and x>5:
	print 'x is not in the list'
print 'End of game'

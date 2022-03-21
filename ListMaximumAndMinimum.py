print 'This program finds the maximum and mininum of numbers using list'
number_list = list()
while True:
    item = raw_input('Enter a number: ')
    if item == 'done':break
    try:
        value = float(item)
    except:
        print 'You have not entered a number'
    number_list.append(value)
    maximum = max(number_list)
    minimum = min (number_list)
print 'Maximum:', maximum, '\n', 'Minimum:', minimum

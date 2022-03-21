print 'Sum and Average of Numbers Using List Method'
a = list()
while (True):
    try:
        item = raw_input('Please Enter A Number. Type Done when you are entered all the numbers.\n')
        if item == 'Done':break
        value = float(item)
        a.append(value)
    except:
        print "You haven't entered a number"
a_sum = sum(a)
a_avg = sum(a)/len(a)
print 'Sum = ', a_sum, 'and Average = ', a_avg

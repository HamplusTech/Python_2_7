### A program to solve for the Mean, Median and Mode of data
##print "A program to solve for the Mean, Median and Mode of data"
##a = list()
##b = list()
##c = dict()
##while True:
##    type_of_data = raw_input("What type of data are you working on? \nType 'G' for GROUPED DATA and 'U' for UNGROUPED DATA. \nType 'END' to end the program\n")
##    try:
##        if type_of_data == 'END' or type_of_data == 'end':
##            break
##        elif type_of_data == 'G' or type_of_data == 'g':
##            print 'Welcome to grouped data analysis'
##            while True:
##                dataX = raw_input("Please enter the numbers (X). Type '000' to stop entering\n")
##                dataFX = raw_input("Please enter the frequency (FX). Type '000' to stop entering\n")
##                try:
##                    if dataX == '000':
##                        break
##                    elif not type(dataX) == str and type(dataFX) == str:
##                        a. append (dataX)
##                        b. append (dataFx)
##                except:
##                    print 'Please do not enter strings'
##                    continue
##            print a
##            print
##            print b
##        elif type_of_data == 'U' or type_of_data == 'u':
##            print 'Welcome to ungrouped data analysis'
##    except:
##        print 'You have not entered the right choice'
##        continue
##
##print 'It is easy'
##


import math
# A program to find the mean, mean and mode
a = list()
b = dict()
count = 0
mean = 0; median = 0; mode = 0
print "Enter the numbers. Type '0000' to stop entering numbers.\n"
while True:
    number = int(input())
    #number = int(number)
    try:
        if (number) == 0000:# or number == "stop":
            break
        elif not type(number) == str:
            a.append(number)
            mean = sum(a)%len(a)
            aSort = sorted(a)
            if type(len(aSort)/2) == float:
                median = aSort[len(aSort)/2 ]
            else:
                median = float((aSort[len(aSort)/2 - 1] + aSort[len(aSort)/2 ]) / 2)
            for nos in numbers:
                if nos in b:
                    b[nos] += 1
                else:
                    b[nos] = 1
                
    except:
        continue
        print "Please enter numerals"
##        continue
print mean, "\t", median, "\t", mode

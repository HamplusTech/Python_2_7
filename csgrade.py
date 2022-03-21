# A simple program to check for score and grade them between 0.0 and 1.0
score = raw_input ('Please enter score between 0.0 and 1.0\n')
try:
    if float(score) >= 0.0 and float(score) <= 1.0:
        if float (score) >= 0.9:
            print 'A'
        elif float (score) >= 0.8:
            print 'B'
        elif float (score) >= 0.7:
            print 'C'
        elif float (score) >= 0.6:
            print 'D'
        else:
            print 'F'
    else:
        print 'Enter score between the specified range. Thanks!'
except:
    print 'Bad Score'

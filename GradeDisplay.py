# A program that prints grade from score. score must be between 0.0 t0 1.0
print 'A program that prints grade from score. score must be between 0.0 t0 1.0'
print 'Programmed by: Hamplus Tech Intl'
print
score = raw_input('Enter your score\n')
try:
    score = float (score)
    if score > 1.0:
        print 'Bad score'        
    elif score >= 0.9:# and score <= 1.0:
        print 'A'
    elif score >=0.8:
        print 'B'
    elif score >= 0.7:
        print 'C'
    elif score >= 0.6:
        print 'D'
    elif score < 0.6:
        print 'F'
except:
    print'Bad score'
    #print 'Please enter a numeral between 0.0 and 1.0'

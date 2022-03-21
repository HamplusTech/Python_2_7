def compute_grade(score):
    try:
        score = float(score)
        if score > 1.0:
            return 'Bad Score'
        elif score >= 0.9:
            return 'A'
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        elif score >= 0.6:
            return "D"
        elif score < 0.6:
            return "F"
    except:
        return 'Bad sco'

print 'The program starts. It takes score and gives you the grade'
a = raw_input('Please enter the score\n')
b = compute_grade(a)
print 'Your grade is\n', b

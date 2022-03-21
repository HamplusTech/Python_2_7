print 'A proram that reads a file, extract a line and converts ...'
fname = raw_input('Please enter a file name like abc.txt\n')
if fname == 'na na boo boo':
    print fname.upper(), "TO YOU - You have been punk'" + 'd!'
else:
    try:
        fhand = open(fname)
        count = 0; total = 0; tline = 0
        for line in fhand:
            count = count + 1
            if line.startswith('X-DSPAM-Confidence: 0.8475'):
                a = line.find(' ')
                b = int(a)
                c = b + 1
                d = line[c:]
                answer = float(d)
                total = total + answer
                print 'In line', count, 'we have', answer
                tline = tline + 1
        print '\nTotal lines having search string:', tline, 'and total of the spam confidence:', total, '\n'
        print 'Average spam confidence:', total/tline
        
    except:
        print 'File cannot be opened:', fname
        exit()


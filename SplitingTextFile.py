fname = 'remeo.txt'
try:
    fhand = open(fname)
except:
    print 'Error Opening File:', fname
answer = list()
print 'Enter file:', fname
for line in fhand:
    line = line.rstrip()
    words = line.split()
##    print words           #to check the lines printed
    if words in answer:continue
    answer = answer + words
##    answer.append(line.split ())      #provides a different list
answer2 = list()
for item in answer:
    new_words = item
##    print new_words             #prints the words in the list answer
    if new_words in answer2:continue     #checks if the word is in the new list
    answer2.append(new_words)
##print answer2.sort()      #sorts but mutates the original list
print sorted(answer2)

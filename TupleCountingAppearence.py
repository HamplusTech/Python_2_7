#Prints the number position of a word in a text
print 'Prints the number position of a word in a text'
text = 'This is a good time to relax. However, it is a pity that some elements\nwill not allow the relaxation. There is urgent need to be fit and to be\nsmart.\n\n\nHampo, JohnPaul A.C.\n07063047037\n08050736053'
aaa = list()
count = 0
words = text.split()
for word in words:
##    if not word in aaa:
##        count = count + 1
##        aaa.append((len(word), word, count))
##    else:
        count = count + 1
        aaa.append((len(word), word, count))
print aaa
print 
print

#Calculates the number of times a word appears in a text
import string
print 'Calculates the number of times a word appears in a text'
txt = 'This is a good time to relax. However, it is a pity that some elements\nwill not allow the relaxation. There is urgent need to be fit and to be\nsmart.\n\n\nHampo, JohnPaul A.C.\n07063047037\n08050736053'
txt = txt.translate(None, string.punctuation)
words = txt.split()
count = dict()
j = list()
for word in words:
       if word not in count:
              count[word] = 1
       else:
              count [word] += 1
for key, val in count.items():
       j.append((len(key), key, val))
jj = tuple(j)
print jj

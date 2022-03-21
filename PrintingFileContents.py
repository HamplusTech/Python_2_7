print 'A program that reads through a file and prints the characters in upper cases'
fname = 'mbox-short.txt'
try:
    fhand = open(fname)
    char = fhand.read() # reads the contents of the file
    length = len(char) # gets the number of the characters
    length = int(length) # converts from string to integer
    answer = char[:length].upper() #converts the contents to upper case
    print answer
except:
    print 'File cannot be opened'
    exit()

#!/usr/bin/python2.7

# Open a file
fo = open("foo.txt", "wb")
fo.write("Python is a great language.\nYeah its great!!\n")
# Close opend file
fo.close()


# Open a file
try:
    fo = open("foo.txt", "r+")
    str = fo.read(60)
except IOError:
    print "Error: can\'t find file or read data"
else:
    print "Written content in the file successfully"
    print "Read String is : ", str
# Close opend file
fo.close()

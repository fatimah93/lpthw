#gets argv
from sys import argv
#unpacks command line arguments
script, filename = argv
#opens the file
txt = open (filename)
#prints the file name variable
print(f"Here's your file {filename}:")
#prints out the files content
print(txt.read())

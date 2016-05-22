#This is a test  script

from sys import argv

script, filename = argv

print "We are going to erase %r" % filename
print "Press control C to abort"
print "Else Return"

raw_input("?")

print "Openning File..."
target = open(filename, 'w')

print "Trunacting the file, Goodbye!"

target.truncate()

print "Now I am going to ask you for three lines"

line1 = raw_input("What is your name?")
line2 = raw_input("Where do you live?")
line3 = raw_input("What do you do?")

print "Now we will write to file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Finally we close the file"
target.close()

 
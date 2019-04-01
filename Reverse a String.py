#  // Reverse a String //

string = str(input('Give me a word! '))
newstr = ''
for char in string:
    newstr = string[::-1]
print (newstr)
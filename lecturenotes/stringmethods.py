'''
Write a function findSubstring() that takes two parameters:
1. line, a string
2. substring, another string
The method returns the number of times substring is found inside line, regardless of the lettercase.
For example,
print(findSubstring('He is here', 'He')) should print 2
print(findSubstring('HE IS HERE', ))
'''

def findSubstring(string, substring):
    lowerString = string.lower() # makes the whole string lowercase
    lowerSubstring = substring.lower() # makes the substring lowercase
    return lowerString.count(lowerSubstring) # returns how many times lowerSubstring appears in lowerString

def findSubstring2(string, substring):
    return string.lower().count(substring.lower()) # the same function but with just one line

print(findSubstring('He is here', 'He')) # prints 2
print(findSubstring2('He is here', 'He')) # prints 2
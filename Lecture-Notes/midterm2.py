
s = ''
s+='u'
print(s, end=' ')
print(s, end=' ')
s+='e'
print(s, end=' ')
print(s, end=' ')
print()
booleans = [ # this list is just [False, True, True, False] when simplified
    True and False,
    not False,
    False or True,
    not not False
]

binary = 0
powerOfTwo = 8
for boolean in booleans: # loops through list of booleans
    if boolean: # if the boolean is true, execute the block
        binary += powerOfTwo # adds powerOfTwo to binary if the above condition is true
    powerOfTwo //= 2 # floor divides powerOfTwo after every loop

print(binary) # prints binary

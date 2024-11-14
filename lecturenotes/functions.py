'''
Write a function isEven() that takes an integer (number) parameter.
The function should return True if the number is even and False otherwise.
Test the function in both situations.
'''

def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
print(isEven(45))
print(isEven(46))

# Execute the code in your IDE and trace its execution

def double(y):
    x = 2
    y *= x
    print('inside double', 'x =', x, 'y =', y)

x, y = 3, 4
print('outside double', 'x =', x, 'y = ', y)
double(y)
print('after double', 'x =', x, 'y = ', y)
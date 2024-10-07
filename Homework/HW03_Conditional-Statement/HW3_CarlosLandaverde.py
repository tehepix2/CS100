'''
Carlos Landaverde
CS 100 Section 001
Homework 3
11/19/2024
'''

# 1
a = 3 # assigning the values to a, b and c
b = 4
c = 5

if a < b:  # checking the conditions
    print("OK")

if c < b:
    print("OK")

if (a + b) == c:
    print("OK")

if (a**2 + b**2) == c**2: # checking if pythagoras' theory holds up in python
    print("OK")

# printing false if the conditions are not true
if a < b:
    print("OK") # these conditions now have an else statement
else:
    print("NOT OK")

if c < b:
    print("OK")
else:
    print("NOT OK")

if (a + b) == c:
    print("OK")
else:
    print("NOT OK")

if (a**2 + b**2) == c**2: # Pythagorean Theorem
    print("OK")
else:
    print("NOT OK")

# 2 -- Sticks

stick_one = float(input("Length of the first stick: "))
stick_two = float(input("Length of the second stick: "))
stick_three = float(input("Length of the third stick: "))

if stick_one ** 2 + stick_two ** 2 == stick_three ** 2: # Pythagorean theorem, assuming these sticks make a 90 degree angle
    print("The sticks can form a triangle.")
elif (stick_one + stick_two == stick_three):
    print("These sticks form a degenerate triangle.")
else:
    print("The sticks cannot form a triangle.")
"""
Carlos Landaverde
CS 100 Section 001
HW 04, October 3, 2024
"""

import turtle # importing the required modules
import math

canvas = turtle.Screen() # initializing the blank canvas
pen = turtle.Turtle() # initializing the pen

side_length = 100 # setting the side lengths
angle_triangle = 360 / 3 # some variables to store the angles for different shapes
angle_pentagon = 360 / 5

pen.forward(side_length) # drawing the triangle
pen.right(angle_triangle)
pen.forward(side_length)
pen.right(angle_triangle)
pen.forward(side_length)
pen.right(angle_triangle)

pen.forward(side_length) # drawing the pentagon
pen.right(angle_pentagon)
pen.forward(side_length)
pen.right(angle_pentagon)
pen.forward(side_length)
pen.right(angle_pentagon)
pen.forward(side_length)
pen.right(angle_pentagon)
pen.forward(side_length)
pen.right(angle_pentagon)

pen.circle(50) # drawing circles with different radii
pen.circle(100)
pen.circle(150)
pen.circle(200)

print("100! = " + str(math.factorial(100))) # printing the factorial of 100
print("Log base 2 of 1000000 = " + str(math.log(1000000, 2))) # printing the log base 2 of one million
print("Greatest common divisor of 63 and 49: " + str(math.gcd(63, 49))) # printing the greatest common divisor of 63 and 49

color = input("Choose a color: ") # prompting the user for a color
width = int(input("Choose a width: ")) # prompting the user for a width
length = int(input("Choose a length: ")) # prompting the user for a length
shape = input("Choose a shape (line, triangle, square): ") # prompting the user for a shape
angle_square = 360 / 4 # storing the angle for a square

pen.width(width) # setting the pen's width
pen.color(color) # setting the pen's color


if shape == "triangle": # drawing a triangle if it is chosen
    pen.forward(length)
    pen.right(angle_triangle)
    pen.forward(length)
    pen.right(angle_triangle)
    pen.forward(length)
    pen.right(angle_triangle)
elif shape == "square": # drawing a square if it is chosen
    pen.forward(length)
    pen.right(angle_square)
    pen.forward(length)
    pen.right(angle_square)
    pen.forward(length)
    pen.right(angle_square)
    pen.forward(length)
    pen.right(angle_square)
elif shape == "line": # drawing a line if it is chosen
    pen.forward(length)
else: # in case the correct shape is not chosen, tell the user their prompt is invalid
    print("Invalid shape entered.")




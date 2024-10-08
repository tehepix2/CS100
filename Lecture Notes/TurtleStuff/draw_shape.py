import turtle
import time

sides = int(input("Enter amount of sides: "))


paper = turtle.Screen()
pen = turtle.Turtle()

turn_angle = 360/sides

for x in range(0,sides):
    pen.forward(50)
    pen.right(turn_angle)

paper.exitonclick()
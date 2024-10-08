import turtle
import time



triangle_size = int(input("Enter triangle size (sides): "))
gap_size = int(input("Enter the size of the gaps between triangles: "))

paper = turtle.Screen()
pen = turtle.Turtle()

pen.color('blue')
pen.up()
pen.goto(-250, 0)
pen.down()
pen.forward(triangle_size)
pen.right(120)
pen.forward(triangle_size)
pen.right(120)
pen.forward(triangle_size)
pen.right(120)
pen.up()
pen.forward(triangle_size + gap_size)
pen.down()

pen.forward(triangle_size)
pen.right(120)
pen.forward(triangle_size)
pen.right(120)
pen.forward(triangle_size)
pen.right(120)
pen.up()
pen.forward(triangle_size + gap_size)
pen.down()

pen.forward(triangle_size)
pen.right(120)
pen.forward(triangle_size)
pen.right(120)
pen.forward(triangle_size)
pen.right(120)
pen.up()
pen.forward(triangle_size + gap_size)
pen.down()

pen.forward(triangle_size)
pen.right(120)
pen.forward(triangle_size)
pen.right(120)
pen.forward(triangle_size)
pen.right(120)


paper.exitonclick()

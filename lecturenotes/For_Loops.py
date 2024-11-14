import turtle

count = 10             #Prints 10 to 0 backwards
for count in range(10, 1, -2):
    print("Hello, " + str(count))


#Use a for loop to create multiple shapes

#Draw shapes with sides 3 - 10

paper = turtle.Screen()
pen = turtle.Turtle()
size = 30

sides = 3
for i in range(0, sides):
    pen.forward(size)
    pen.right(360 / sides)



turtle.Screen().exitonclick()
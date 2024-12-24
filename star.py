import turtle

turtle.Screen().bgcolor("orange")

sc = turtle.Screen()
sc.setup(400, 300)
turtle.title("welcome to turtle window")
door = turtle.Turtle()

door.forward(100)

door.left(120)
door.forward(100)

door.left(120)
door.forward(100)

door.penup()
door.right(150)
door.forward(50)

door.pendown()
door.right(90)
door.forward(100)

door.right(120)
door.forward(100)

door.right(120)
door.forward(100)

turtle.done()
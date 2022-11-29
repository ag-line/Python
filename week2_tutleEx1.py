import turtle

t = turtle.Turtle()
t.shape("turtle")

screen = turtle.Screen()
screen.bgcolor("lightblue")

t.left(45)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(-90)
t.forward(50)

t.left(90)
t.forward(50)
t.left(90)
t.forward(100)

turtle.done()
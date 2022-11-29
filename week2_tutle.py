import turtle

t = turtle.Turtle()
t.shape("turtle")

screen = turtle.Screen()
screen.bgcolor("lightblue")

t.fillcolor("yellow")
t.begin_fill()
t.goto(0,0)
t.goto(200,0)
t.goto(200,180)
t.goto(0,180)
t.goto(0,0)
t.end_fill()

t.penup()
t.fillcolor("blue")
t.goto(20,20)
t.pendown
t.begin_fill()
t.goto(180,20)
t.goto(180,150)
t.goto(20,150)
t.goto(20,20)
t.end_fill()

t.penup()
t.fillcolor("pink")
t.goto(30,30)
t.pendown
t.begin_fill()
t.goto(130,30)
t.goto(130,130)
t.goto(30,130)
t.goto(30,30)
t.end_fill()

turtle.done()
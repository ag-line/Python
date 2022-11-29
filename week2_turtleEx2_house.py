import turtle

t = turtle.Turtle()
t.shape("turtle")

screen = turtle.Screen()
screen.bgcolor("lightblue")

t.fillcolor("cyan")

t.begin_fill()
t.goto(0,0)
t.goto(200,0)
t.goto(100,100)
t.goto(0,0)
t.end_fill()

t.fillcolor("brown")
t.begin_fill()
t.goto(200,0)
t.goto(200,-100)
t.goto(0,-100)
t.goto(0,0)
t.end_fill()

t.penup()
t.fillcolor("pink")
t.goto(50,-30)
t.pendown
t.begin_fill()
t.goto(80,-30)
t.goto(80,-60)
t.goto(50,-60)
t.goto(50,-30)
t.end_fill()

turtle.done()
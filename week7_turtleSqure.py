import turtle

t= turtle.Turtle()
t.shape("turtle")

def squre(leng):
  t.pendown()
  for i in range(4):
    t.forward(leng)
    t.left(90)
  t.penup()

for i in range(3):
  squre(100)
  t.forward(120)

turtle.done()
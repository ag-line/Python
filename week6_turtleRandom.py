import turtle
import random

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(6)
n = 0
for i in range(20):
    n+=1
    length = random.randint(1,100)
    angle = random.randint(-180,180)
    t.forward(length)
    t.right(angle)
    print(n,"번째: ",length,angle)
    if n == 10:
      t.reset()
turtle.done()

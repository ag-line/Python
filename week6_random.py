import turtle
import random

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(2)
colors = ['orange','red','blue','violet','green']
for i in range(10):
    #t.reset()
    col = random.choice(colors)
    n = random.randint(3,11)
    t.color(col)
    print(i+1,n,col)
    
    if n == 11:
        for i in range(5):
            length = random.randint(1,100)
            angle = random.randint(-180,180)       
            t.forward(length)
            t.right(angle)
    for j in range(n):
        t.forward(50)
        t.left(360/n)
    
turtle.done()

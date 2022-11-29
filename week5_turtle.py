import turtle
import random

t= turtle.Turtle()
t.shape("turtle")

cnt = 0
for i in range(20):
    leng = random.randint(50,100)
    angle = random.randint(30,170)
    cnt += 1
    t.forward(leng)
    t.left(angle)
    print(cnt)
    if cnt == 10:
        t.reset()
        
turtle.done()
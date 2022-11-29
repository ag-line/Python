import turtle

t= turtle.Turtle()
t.shape("turtle")

def calc_rect(w,h):
  return w*h, 2*(w+h)
  #(f"넓이는 {w*h} 둘레는 {2*(w+h)}") 

def draw_rect(w,h):
  t.fillcolor("red")
  t.begin_fill()
  t.forward(w)
  t.left(90)
  t.forward(h)
  t.left(90)
  t.forward(w)
  t.left(90)
  t.forward(h)
  t.left(90)
  t.end_fill()

area, length = calc_rect(100,200)
rectInfo='[area:'+str(area)+', length: '+str(length)+']'	
turtle.write(rectInfo,move=False,align='left',font=("Arial",12,"normal"))

draw_rect(100,200)
t.reset()
draw_rect(300,200)

turtle.done()
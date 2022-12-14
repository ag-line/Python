class TV:
  #객체를 재사용하기 위해 class로 만듬 ->객체지향 
  def __init__(self,channel,vol,on):
    self.channel = channel
    self.vol = vol
    self.on = on
  def show(self):
    print(self.channel, self.vol, self.on)
  def setChannel(self, channel):
    self.channel = channel
  def getChannel(self):
    return self.channel

t1 = TV(9,10,True)
t1.show()
t1.setChannel(11)
print(t1.getChannel())

t2 = TV(9,10,True)
t2.show()
t2.setChannel(11)
print(t2.getChannel())

import math

class Circle:
  def __init__(self, radius = 0):
    self.radius  = radius
  def getArea(self):
    return math.pi * self.radius * self.radius
  def getPerimeter(self):
    return 2* math.pi * self.radius

c1 = Circle(10)
print("원의 면적 : ", int(c1.getArea()))
print("원의 둘레 : ", c1.getPerimeter())

c2 = Circle(50)
print("원의 면적 : ", c2.getArea())
print("원의 둘레 : ", int(c2.getPerimeter()))
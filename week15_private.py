## private
class Stu:
  def __init__(self, name = None, age=0):
    self.name = name
    self.__age = age
s = Stu("hong",24)
print(s.name) #hong
  # print(s.__age) #AttributeError: 'Stu' object has no attribute '__age'

#setter getter
class Student:
  def __init__(self, name = None, age=0):
    self.__name = name
    self.__age = age
  def getAge(self):
    return self.__age
  def getName(self):
    return self.__name
  def setAge(self, age):
    self.__age = age
  def setName(self, name):
    self.__name = name

sTU = Student("hong",24)
AST = sTU #참조공유

#print(sTU.__age) #AttributeError: 'Student' object has no attribute '__age'
print(sTU.getName(), sTU.getAge()) #hong 24
sTU.setName("KIm")
sTU.setAge(30)
print(sTU.getName(), sTU.getAge()) #KIm 30

class BankAccount:
  def __init__(self):
    self.__balance = 0
  def withdraw(self, amount):
    self.__balance -= amount
    print("withdraw: ",amount,"won")
    return self.__balance
  def deposit(self, amount):
    self.__balance += amount
    print("deposit: ", amount,"won")
    return self.__balance

a = BankAccount()
b = a #참조공유
#print(a.__balance) #AttributeError: 'BankAccount' object has no attribute '__balance'

print("balance: ", a.deposit(100000))
#deposit:  100000 won
#balance:  100000

print("balance: ", a.withdraw(5000))
#withdraw:  5000 won
#balance:  95000


class Rectangle:
  def __init__(self, w = 0, h = 0):
    self.__w  = w
    self.__h  = h
  ##getter func
  def get_w(self):
    return self.__w
  def get_h(self):
    return self.__h

  ##setter func
  def set_w(self,w):
    self.__w = w
  def set_h(self,h):
    self.__h = h

  def calcArea(self):
    return self.__w * self.__h

  def calcPerimeter(self):
    return 2*(self.__w + self.__h)

r1 = Rectangle(10,20)

print(r1.get_w(), r1.get_h()) 
print("사각형의 면적 : ", r1.calcArea())
print("사각형의 둘레 : ", r1.calcPerimeter())
print("↓")

r1.set_w(40)
r1.set_h(30)
print(r1.get_w(), r1.get_h()) 
print("사각형의 면적 : ", r1.calcArea())
print("사각형의 둘레 : ", r1.calcPerimeter())

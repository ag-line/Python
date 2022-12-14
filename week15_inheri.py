class Person():
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
  def getName(self):
    return self.__name
  def getAge(self):
    return self.__age

class Student(Person):
  def __init__(self, name, age, depart, gpa):
    super().__init__(name,age)
    self.__depart = depart
    self.__gpa = gpa

  def getDepart(self):
    return self.__depart

  def getGpa(self):
    return self.__gpa
    
  def show(self):
    print(super().getName(), super().getAge(), self.__depart, self.__gpa)
          ##부모객체에 접근하는 법 super().---- 
          # // but, private변수는 부모객체의 함수를 통해서 접근 

p = Person("hong",45) #부모
print(p.getName() , p.getAge())
s = Student("kim",23,"com",4.5)
s.show()

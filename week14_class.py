#클래스와 객체를 통해 코드의 재사용 완벽하게 됨
class Counter:
  def __init__(self):
    self.count = 0
  def increment(self):
    self.count += 1

#a객체
a = Counter()
print(a.count)
a.increment()
print(a.count)

#b객체
b = Counter()
print(b.count)
b.increment()
print(b.count)

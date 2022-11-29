num = 100 #전역변수
print(f"초기: {num}")

def func1():
  print(f"func1: {num}")

def func2():
  global num #전역변수로 선언
  num = 200
  print(f"func2: {num}")

def func3():
  num = 300 #지역변수
  print(f"fun3: {num}")

func1()
func2()
func3()
print(f"마지막: {num}")

""" 따로 나눌 경우 x혹은 y에 정수를 입력하지 않을 경우 
다음 try로 넘어가서 x,y가 정의 되지 않았다고 오류 뜸
try:
  x = int(input("x: "))
  y = int(input("y: "))
except ValueError:
  print("정수를 입력하세요")
try:
  print(f"{x}/{y} = {x/y}")
except ZeroDivisionError as e:
  print(e) #division by zero
 """

#try -catch : try에서 예외 발생시 정상동작하도록 예외처리를 함
try:
  x = int(input("x: "))
  y = int(input("y: "))
  print(f"{x}/{y} = {x/y}")
except ValueError:
  print("정수를 입력하세요")
except ZeroDivisionError as e:
  print(e) #division by zero
  print("0으로 나눌 수 없습니다 y를 다시 입력하세요 입력하세요") #내가 설정한 구문

try:
  f = open("num.txt","r")
except IOError:
  print("파일을 열 수 없습니다")
#대소문자 변환
s = 'Break'
print(s.upper())  #BREAK
print(s.lower())  #break
print(s)  #Break

#문자열검사
print('hello'.islower())  #True
print('HELLO'.isupper())  #True
print('abc12'.isalpha())  #False
print('abcde'.isalnum())  #True 영문자와 숫자로만 구성되는 경우
print('12345'.isdecimal())  #True
print('\n'.isspace()) #True

def createPw():
  while True:
    passwd = input("패스워드를 입력하세요: ")
    if len(passwd) > 8 :
      print("8자 이상으로 입력하세요: ")
      continue
    elif not(passwd.isalnum()):
      print("숫자와 문자를 조합하여 입력하세요: ")
      continue
    
    passwd2 = input("다시 패스워드를 입력하세요: ")
    if passwd == passwd2:
      print("입력 완료")
      break
    else:
      print("패스워드가 다릅니다")
      continue
#createPw()

def pythonchk(mlist):
  for s in mlist:
    if s.endswith(".py"):
      print(s)
    if s.startswith("text"):
      print(s)
#pythonchk(["ex.py","ex1.c","text.js","ex3.py"]) #ex.py text.js ex3.py

def input_score():
  stu = input("성적을 입력하세요(번호 이름 성적): ") #1 김은선 239
  mylist = stu.split() #공백으로 구분
  print(mylist) #['1', '김은선', '239']
  num = mylist[0]
  name = mylist[1]
  score = mylist[2]
  print(f"{num}번 {name}님의 성적은{score}점입니다") #1번 김은선님의 성적은239점입니다
#input_score()

def input_HP():
  hp =input("핸드폰 번호를 입력하세요(숫자만): ") #01056581327
  hp = '-'.join([hp[0:3],hp[3:7],hp[7:]])
  print(hp) #010-5658-1327
input_HP()
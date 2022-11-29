#문자열 역슬라이스는 출력안함
print('this is kim\'s dog')#this is kim's dog
print("this is kim\'s dog")#this is kim's dog

#원시 문자열 r'string'형태로 문자열 그대로 출력
print(r'this is kim\'s dog') #this is kim\'s dog

#문자열 슬라이싱
s = 'Monty Python'
print(s[6:10]) #Pyth
print(s[-2:]) #on
print(s[:-5],"+",s[4:],"=", s[:-5]+s[4:]) #Monty P + y Python = Monty Py Python

#in/ not in 연산자
print('Python' in s) #True
print('python' in s) #False (대소문자 구분)

#문자열 안에 문자열 넣기
name = 'kim'
age = '21'
print('이름은 %s, 나이는 %s'%(name,age)) #이름은 kim, 나이는 21
print('이름은'+ name +', 나이는 '+age) #이름은 kim, 나이는 21

#문자열 비교
print('apple' < 'banana') #True
print('apple' < 'abc') #False

#회문찾기(앞뒤가 같은문자열)
def palchk():
  origin = input("str")
  rev = origin[::-1] #역순으로 복사

  if origin == rev:
    print("회문입니다")
  else: print("아닙니디")
palchk()
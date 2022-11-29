import re

def searchXman(str):
  ptn = "^X-Men.*"
  if re.search(ptn, str):
    print(str)
  else:
    print("x-men 시리즈가 아닙니다")

movie = [
  "X-Men: first Class",
  "X-Men: Days of future past",
  "X-Men orgin: wolVreine",
  "starWars:A new Hope",
  "starWars: Return"
  ]
for i in movie:
  searchXman(i)

def chkText(f,ptn):
  for line in f:
    found = re.search(ptn,line)
    if found:
      print(found.group()) #첫번째줄의 시작숫자, 두번째줄 시작숫자 출력
      print(line) #라인전체 출력됨

""" f = open("week12_text")
chkText(f,"^[0-9]") # 1 0
print("===========")
chkText(f,"^[0-9]+") # 1 010227
print("===========")
chkText(f,"\d{6}-\d{7}") # 010227-2559043
print("===========")
chkText(f,"[A-Za-z]$") # A """

def cntText(f,ptn):
  data = f.read()
  word_dic = {} #공백 dic 생성
  #공백으로 분리해서 저장
  for w in data.split(): 
    if re.search(ptn,w):
      if w in word_dic:
        word_dic[w] += 1
      else:
        word_dic[w] = 1
  for w in word_dic.items():
    print(w)

f = open("week12_text2")
#영어가 포함된것만 출력 
cntText(f,"[A-Za-z]")
""" 
('hong', 1)
('A', 3)
('python', 3)
('phone', 1)
('number', 1)
('is', 1)
('network', 1)
('network,', 1)
('c++', 1)
('fmlkqjqoijooq', 1)
('foqoj', 1)
단어 뒤에 콤마 포함되어 있을 경우 카운트에 포함안됨"""
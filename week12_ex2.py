import re
def cntWord(f,ptn):
  data = f.read()
  #공백 dic 생성
  word_dic = {} 
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
cntWord(f,"^[0-9]{2}") 
#('100', 1) ('001201-2086756', 1) ('010-111-2222', 1) ('12345676', 1) ('12123', 1)
cntWord(f,"^[B-Z]") 
#('Python', 3) ('Network', 2) ('C++', 1)

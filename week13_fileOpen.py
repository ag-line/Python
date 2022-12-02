""" f = open("text.txt","w")
f.write("파이썬 쓰기")
f.close() """

""" f = open("text.txt","a")
f.write("파이썬 파일에 덧붙여쓰기")
f.close()  """


""" #읽어서 변수에 저장하여 print
f = open("text.txt","r",encoding='utf-8')
buf = f.read()
print(buf)
f.close() 
#한글 인코딩 형식 다르게 저장 되면 에러뜸->
 """
#with문으로 쓰기
with open("text.txt","w",encoding='utf-8') as f:
  f.write("witha문으로 작성\n")

#with문으로 읽기
with open("text.txt","r",encoding='utf-8') as f:
  buf = f.read()
print(buf)

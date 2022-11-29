Mlist = [1,"김",3,"은",5,"선",7]

#인덱스이용 탐색
for i in range(len(Mlist)):
  print(Mlist[i])

#for-each구문 이용 탐색
for elements in Mlist:
  print(elements)

#해당 값의 인덱스 탐색
inde = Mlist.index(3)
print("'선' 의 인덱스: ",inde)

if 4 in Mlist:
  print("있습니다")
else:
  print("없습니다")

#맨 뒤 삽입
Mlist.append(9)   # Mlist = [1,"김",3,"은",5,"선",7,9]
#해당인덱스(0)에 삽입
Mlist.insert(0,"나")  # Mlist = ["나",1,"김",3,"은",5,"선",7,9]

#해당 인덱스의 요소 삭제
dele = Mlist.pop(-1) 
print(Mlist)
#해당요소 삭제
Mlist.remove(1) 
Mlist.remove("나") 
print(Mlist)  # Mlist = ["김",3,"은",5,"선",7]

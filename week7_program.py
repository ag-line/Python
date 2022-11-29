num = []
name =[]
score =[]

def menuPrint():
  print("================================")
  print("1. 성적입력(번호, 이름, 점수)")
  print("2. 성적삭제(번호)")
  print("3. 성적검색(이름)")
  print("4. 통계보기(평균, 최고점, 최저점)")
  print("5. 성적출력")
  print("0. 종료")
  print("================================")
  global menu
  menu = int(input("메뉴선택: "))
  if menu == 1:
    inputData()
  elif menu == 2:
    deleteData()
  elif menu == 3:
    searchData()
  elif menu == 4:
    view()
  elif menu == 5:
    printScore()

def inputData():
  n = int(input("번호: "))
  num.insert(n,n)
  name.insert(n,input("이름: "))
  score.insert(n,int(input("점수: ")))
  print(f"학생수: {len(num)}")
  for i in range(len(num)):
    print(f"{num[i]} {name[i]} {score[i]}점")
  print("!!입력완료!!")
  menuPrint()

def deleteData():
  n = int(input("번호: "))
  if n in num:
    delete_num = num.index(n)
    num.pop(delete_num)
    name.pop(delete_num)
    score.pop(delete_num)  
    print(f"학생수: {len(num)}")
    for i in range(len(num)):
      print(f"{num[i]} {name[i]} {score[i]}점")
    print("!!삭제완료!!")
  else:
    print(f"{n}번은 없습니다")
  menuPrint()


def searchData():
  searchName = input("이름: ")
  if searchName in name:
    n = name.index(searchName)
    print(f"{num[n]} {name[n]}: {score[n]}점")
  else:
    print(f"찾으시는 {searchName}님이 없습니다")
  menuPrint()

def view():
  n = score.index(max(score))
  print(f"{num[n]} {name[n]}님이 {score[n]}점으로 최고점")
  i = score.index(min(score))
  print(f"{num[i]} {name[i]}님이 {score[i]}점으로 최저점")
  print(f"총 평균: {sum(score) // len(num)}")
  menuPrint()

def printScore():
  for i in range(len(num)):
    print(f"{num[i]} {name[i]} {score[i]}점")
  menuPrint()
  
while True:
  menuPrint()
  if menu == 0:
    break

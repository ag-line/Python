import random

def getLotto():
  myList=[]
  while len(myList) != 6:
    num = random.randint(1,45)
    if num not in myList:
      myList.append(num)
  return myList
lottoList = getLotto()
print(lottoList)
def inputData(n):
  myList = []
  for i in range(n):
    temp = []
    temp.append(int(input("학번: ")))
    temp.append(input("이름: "))
    temp.append(int(input("점수: ")))
    myList.append(temp)
  print("==inputData==")
  print(myList)  
  return myList

def saveFile(myList):
  global mStr
  with open("score.txt","w",encoding='utf-8') as f:
    for i in range(len(myList)):
      mStr = ' '.join(map(str,myList[i]))
      print("===saveFile===")
      print(mStr)
      if i == (len(myList)-1):
        f.write(mStr)
      else:
        f.write(mStr+'\n')

def readFile(fileName):
  f = open(fileName,"r",encoding='utf-8')
  row = f.read().split("\n")
  keys = []
  values = [] 
  myDic = {}
  print("===readFile===")
  for line in row:
    line = line.split()
    keys.append(int(line[0]))
    values.append(line[1:])
  #dic으로 저장
  for i in range(len(keys)):
    myDic[keys[i]] = values[i]
    print(myDic)
  return myDic

def searchData(keys, myDic):
  print("==searchData==")
  print(keys,myDic[keys])

myList = inputData(3)
saveFile(myList)
myDic = readFile("score.txt")
searchData(1,myDic)
  
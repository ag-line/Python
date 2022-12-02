import csv

#list사용하여 파일 읽기
def csvRead(f):
  data = csv.reader(f)
  dataList = []
  for line in data:
    dataList.append(line)
  print(dataList) 
  return dataList

#dic 사용하여 출력
def crateDic(data):
  dataDic = {}
  for row in data:
    key = row[0]
    val = row[1:]
    dataDic[key] = val
  print(dataDic) 
  return dataDic

def searchcode(key,dic):
  print(dic.get(key,"no key"))

f = open('Ncode.csv','r')
data = csvRead(f)
#[['KR', 'Korea', 'Seoul'], ['US', 'USA', 'Washington'], ['JP', 'Japan', 'Tokyo'], ['CN', 'China', 'Beijing'], ['RU', 'Rusia', 'Mosow']]

mDic = crateDic(data)
#{'KR': ['Korea', 'Seoul'], 'US': ['USA', 'Washington'], 'JP': ['Japan', 'Tokyo'], 'CN': ['China', 'Beijing'], 'RU': ['Rusia', 'Mosow']}

searchcode("KR",mDic) #['Korea', 'Seoul']
searchcode("NU",mDic) #no key
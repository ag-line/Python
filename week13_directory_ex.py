import os

#os.chdir("..\\") #상위 디렉토리로 변경하여 출력됨
#C:\Users\dmstj\.vscode <class 'str'>
#b'C:\\Users\\dmstj\\.vscode' <class 'bytes'>

""" 
os.mkdir("dir1") #디렉토리 생성
os.chdir("dir1") #이 디렉토리로 이동하여 출력됨 """

path = os.getcwd()
path_binery = os.getcwdb()

print(path,type(path))  #C:\Users\dmstj\.vscode\python <class 'str'>
print(path_binery,type(path_binery))  #b'C:\\Users\\dmstj\\.vscode\\python' <class 'bytes'>

#print(os.listdir()) #파일명 다 출력됨

def findFile(name):
  files = os.listdir()
  for n in files:
    if os.path.isfile(n):
      #name으로 끝나는 파일명 모두 출력
      if n.endswith(name):
        print(n) 

findFile(".csv") #Ncode.csv

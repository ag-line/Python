#list -> set
Numlist = set([1,2,3,1,4,5])
print(Numlist, type(Numlist)) #{1, 2, 3, 4, 5} <class 'set'>
strList = set("ABCADE")
print(strList, type(strList)) #{'B', 'A', 'C', 'D', 'E'} <class 'set'>

#set 연산
letter = set("letter")
letter.add("add")
print(letter) #{'t', 'e', 'l', 'r', 'add'} 순서가 없어서 실행시마다 다른 순서로 출력됨

for v in letter:
  print(v,end=',')
print() #t,l,e,r,add,

letter.remove("add")
print(letter) #{'t', 'r', 'l', 'e'}

letter.clear()
print(letter) #set()

#set 함축
aList = [1,2,3,4,5] #리스트
hamchuk_set = {x for x in aList if x%2==0} #list->set변경 함축 
print(hamchuk_set, type(hamchuk_set)) #{2, 4} <class 'set'>
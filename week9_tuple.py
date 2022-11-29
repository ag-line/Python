myTuple = (10,"apple",3.14)
#원소가 한개일 경우에는 끝에 쉼표 필수
myTuple2 = (10,)

""" 튜플은 값 변경 불가
myTuple[0] = 100 
  #print(myTuple) TypeError: 'tuple' object does not support item assignment """

print(f"myTuple (id:{id(myTuple)}): {myTuple}") 
  #myTuple (id:2823205447808): (10, 'apple', 3.14)

MyList = list(myTuple) #튜플->리스트
print(MyList) #[10, 'apple', 3.14]
print(myTuple) #(10, 'apple', 3.14)
#리스트로 변경한 후 다시 튜플로 생성시 값변경 가능
MyList[0] = 100
MyList.append(200)
myTuple = tuple(MyList) #리스트->튜플
print(myTuple) #(100, 'apple', 3.14, 200)

print(f"myTuple (id:{id(myTuple)}): {myTuple}") 
  #myTuple (id:2296071422896): (100, 'apple', 3.14, 200)
  #처음의 id값과 다름 = 값을 변경한 후에 새 튜플을 만든것
myTuple += ("banana","kiwi")
print(f"myTuple (id:{id(myTuple)}): {myTuple}") 
  #myTuple (id:1804720032544): (100, 'apple', 3.14, 200, 'banana', 'kiwi')

for i in myTuple:
  print(i)
# 100
# apple
# 3.14
# 200
# banana
# kiwi
for t in enumerate(myTuple):
  print(t)
# (0, 100)
# (1, 'apple')
# (2, 3.14)
# (3, 200)
# (4, 'banana')
# (5, 'kiwi')

for idx,v in enumerate(myTuple):
  print(idx,v)
# 0 100
# 1 apple
# 2 3.14
# 3 200
# 4 banana
# 5 kiwi
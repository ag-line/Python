mySet = set ()
for i in range(1,11):
  mySet.add(i)
print(mySet) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

myList = [k for k in range(1,11)]
print(set(myList))#{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

word = "Oh my love is red red rose"
aSet = word.split(" ")
print(aSet) 
#['Oh', 'my', 'love', 'is', 'red', 'red', 'rose']
print(len(aSet)) 
#7

bSet = set(aSet)
print(bSet) 
#{'love', 'Oh', 'my', 'red', 'rose', 'is'}
print(len(bSet))
print(max(bSet)) #rose
print(min(bSet)) #Oh
#6
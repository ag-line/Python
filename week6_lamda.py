def func1(x):
  return x+10

func2 = lambda x : x+10

print(func1(10))
print(func2(10))

func3 = lambda x,y : x+y
print(func3(10,3))

myList = [1,2,3,4,5,6,7]
 #func4 = map(lambda x : x**2, myList) 리스트를 x에 각각 뿌림
func4 =list(map(lambda x : x**2, myList)) #list로 만들어야 출력가능
print(func4)

#디폴트인수
def add1(a,b,c,d,e=10):
  		print (a,b,c,d,e)
add1(0,3,4,5)
#키워드인수
def add2(a,b,c,d,e):
  print("a=",a," b=",b," c=",c," d=",d," e=",e)
add2(a=4,d=8,b=5,c=6,e=7)
add2(4,b=5,c=6,d=7,e=8)

#람다함수
add3 = lambda a,b,c,d,e : a+b+c+d+e 
print(add3(1,2,3,4,5))

my = [1,2,3,4,5]
lam = list(map(lambda x:x**2,range(1,6)))
print(my)
print(lam)

#가변인수
def add4(*num):
  print(num)
add4(1,2,3,4,5)
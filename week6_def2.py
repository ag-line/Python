def varfunc(*args):
  print(f"가변인수{args} 의 타입은 {type(args)}")
varfunc(10,20)
varfunc(10,20,30)

def add(*num):
  sum = 0
  for i in num:
    sum += 1
  return sum

print(add(10,20))
print(add(10,20,30))

def sum(*a):
  print(a)
alist = [1,2,3,4,5]
sum(*alist)

alist.remove(4)
print("--",alist)
alist.pop()
print(alist)
del alist[2]
print(alist)
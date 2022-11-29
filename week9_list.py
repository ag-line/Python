from audioop import reverse
import re
from unittest import result


values = [i for i in range(1,11)]
print(values)
values2 = [2*i for i in range(1,6)]
print(values2)
values3 = [i**2 for i in range(1,11)]
print(values3)

list1 = [1,2,3]
list2 = [4,5,6]
print(list1+list2)
print(list1 *2)
print(list1 == list2)

values_1 = [1,3,2,5,4,6]
values_1.append(10)
print(values_1)
values_1.pop()
print(values_1)
values_1.insert(1, 20)
print(values_1)
del values_1[0:3]
print(values_1)
values_1.sort(reverse=True)
print(values_1)

alist = [x+y for x in ["hi","good"] for y in ["work", "bye"]]
print(alist)

sliceing = [1,2,3,4]
sliceing[1:4] = [5,6,7]
print(sliceing)

Alist = [1,2,3,4,5,6,7]
Blist = [2*x for x in Alist]
print(Blist)
deep = Alist.copy()
print(deep)
Alist[0] = 0
print(deep)
print(Alist)

valuse = [1,2,3,4,5,6,7,8,9,10]
res = 0
for i in range(0, len(valuse),2):
  res = res + valuse[i]
print(res)

Mlist = [[1,2,3],[4,5,6],[7,8,9]]
print(Mlist[0][1])
print(Mlist[1][2])
print(Mlist[1])
values = [i for i in range(1,11)]
print(values) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
values2 = [2*i for i in range(1,6)]
print(values2) #[2, 4, 6, 8, 10]
values3 = [i**2 for i in range(1,11)]
print(values3) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]    

list1 = [1,2,3]
list2 = [4,5,6]
print(list1+list2) #[1, 2, 3, 4, 5, 6]
print(list1 *2) #[1, 2, 3, 1, 2, 3]
print(list1 == list2) #False

values_1 = [1,3,2,5,4,6]
values_1.append(10)
print(values_1) #[1, 3, 2, 5, 4, 6, 10]
values_1.pop()
print(values_1) #[1, 3, 2, 5, 4, 6]
values_1.insert(1, 20)
print(values_1) #[1, 20, 3, 2, 5, 4, 6]
del values_1[0:3]
print(values_1) #[2, 5, 4, 6]
values_1.sort(reverse=True)
print(values_1) #[6, 5, 4, 2]

alist = [x+y for x in ["hi","good"] for y in ["work", "bye"]]
print(alist) #['hiwork', 'hibye', 'goodwork', 'goodbye']

sliceing = [1,2,3,4]
sliceing[1:4] = [5,6,7]
print(sliceing) #[1, 5, 6, 7]

Alist = [1,2,3,4,5,6,7]
Blist = [2*x for x in Alist]
print(Blist) #[2, 4, 6, 8, 10, 12, 14]
deep = Alist.copy()
print(deep) #[1, 2, 3, 4, 5, 6, 7]
Alist[0] = 0
print(deep) #[1, 2, 3, 4, 5, 6, 7]
print(Alist) #[0, 2, 3, 4, 5, 6, 7]

valuse = [1,2,3,4,5,6,7,8,9,10]
res = 0
for i in range(0, len(valuse),2):
  res = res + valuse[i]
print(res) #25

Mlist = [[1,2,3],[4,5,6],[7,8,9]]
print(Mlist[0][1]) #2
print(Mlist[1][2]) #6
print(Mlist[1]) #[4, 5, 6]
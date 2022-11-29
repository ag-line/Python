def minmax(item):
  return min(item),max(item)
t = (1,2,3,4,5)
V = minmax(t) #리턴값을 하나로 패킹 (리턴값개수 상관없이)
print(V) #(1, 5)
minV, maxV = minmax(t)
print(minV,maxV) #1 5
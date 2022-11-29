a = [1,2,3,4,5]
b = [1,3,3,4,5,6,7]
c = []
for elements in a:
  if elements in b:
    c.append(elements)
print(c)
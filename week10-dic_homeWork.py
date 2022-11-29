dic = {"kim":23, "kang":34, "park":28}
print(dic) #{'kim': 23, 'kang': 34, 'park': 28}

print(dic.keys())  #dict_keys(['kim', 'kang', 'park'])
print(dic.values())  #dict_values([23, 34, 28])

dic["han"] = 25
print(dic)  #{'kim': 23, 'kang': 34, 'park': 28, 'han': 25}

myList = ["abc","aa","adddd","a"]
mydic = {a:len(a) for a in myList}
#print(mydic)
for key in mydic:
  print(key,":",mydic[key])
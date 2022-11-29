aList = set([1,2,3,4,5]) #list->Set
aSet = {x for x in aList if x%2==0} #list->set변경 함축 

#부분집합
print(aSet.issubset(aList)) #True 
print("list:",aList,"set:",aSet) #list: {1, 2, 3, 4, 5} set: {2, 4}

#동일
print(aList == aSet) #False

#합집합
print(aList | aSet) #{1, 2, 3, 4, 5}
print(aList.union(aSet)) #{1, 2, 3, 4, 5}

#교집합
print(aList & aSet) #{2, 4}
print(aList.intersection(aSet)) #{2, 4}

#차집합
print(aList - aSet) #{1, 3, 5}
print(aList.difference(aSet)) #{1, 3, 5}

txt = input("text")
# when i first said i loved only u maggie and you said you loved  only me
word = txt.split(" ")
# ['when', 'i', 'first', 'said', 'i', 'loved', 'only', 'u', 'maggie', 'and', 'you', 'said', 'you', 'loved', '', 'only', 'me']
print(word)
#{'only', 'i', 'u', 'you', 'and', 'me', 'maggie', 'first', 'said', 'when', 'loved'} 중복제거
print(set(word))

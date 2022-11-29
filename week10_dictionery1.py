#항목 탐색하기
dic = {"kr":"seoul","usa":"wachington","uk":"london"}
print(dic["kr"]) #seoul

print(dic.get("ammerica","NO key")) #NO key -> 오류처리해줌
#print(dic["ammerica"]) #KeyError: 'ammerica' 프로그램이 오류로 중단됨

if "usa" in dic:
  print("Yes")

#항목추가: 딕셔너리명["key"] = "Value"
dicc = {}
dicc["KR"] = "Seoul"
dicc["usa"] = "wachington"
dicc["uk"] = "london"
""" dicc["Kim"] = "Eunseon"
dicc["park"] = "ES"
 """
print(dicc) #{'KR': 'Seoul', 'usa': 'wachington', 'uk': 'london'}

#항목삭제
#city = dicc.pop("uk") 
#만약 키값이 없다면 오류 나기 때문에 아래와 같이 예외처리해줌
if "uk" in dicc:
  city = dicc.pop("uk")
print(city) #london (삭제된 키의 값이 출력)

#항목 방문
for key in dicc:
  print(key,":",dicc[key])
  #KR : Seoul
  #usa : wachington

for item in dicc.items():
  print(item) 
  #('KR', 'Seoul')
  #('usa', 'wachington')

#정렬 순서/글자순
for key in sorted(dicc.keys()):
  print(key) 
  #KR 
  #usa

#키, 값 가져오는 함수
print(dicc.values()) #dict_values(['Seoul', 'wachington'])
print(dicc.keys()) #dict_keys(['KR', 'usa'])

#딕셔너리 함축
mLi = [k for k in range(1,11)]
  # x:x == 키:값 수식임
mdic = {x:x for x in mLi if x%2 == 0}
print(mdic) #{2: 2, 4: 4, 6: 6, 8: 8, 10: 10}
import re

str = "My phone number is 010-3048-5818"
def searchptn(ptn,str):
  found = re.search(ptn,str)
  if found:
    print(found.start(), found.end(), found.span()) #19 32 (19, 32)
    print(found.group()) #010-3048-5818
  else:
    print("찾는패턴 ",ptn,"은 없습니다.")
  """ print(found) 
        <re.Match object; span=(19, 32), match='010-3048-5818'>
        span = str의 19~23인덱스 범위출력, match = 찾은 패턴 
  """

searchptn(r'010-\d\d\d\d-\d\d\d\d',str) #r이하 문자열 형태 그대로
searchptn("abc",str)
searchptn(".+",str) #문자가 하나이상 반복되는 (str 전부 출력)
searchptn("^[0-9]",str) #0-9사이의 숫자로 시작하는 (None)
searchptn("[0-9]+$",str) #숫자로 1회이상반복하여 끝나는 (5818)
searchptn("[0-9]*$",str) #숫자로 0회이상반복하여 끝나는 (5818)
#핸드폰 번호 찾는 패턴
searchptn("\d{3}-\d{4}-\d{4}",str) #(010-3048-5818)

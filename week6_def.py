#함수는 인터프리트 언어이기 때문에 순서가 중요
#함수 호출 전에 함수선언, 다른 함수에서 호출은 가능
def print_info(r):
  area = get_area(r)
  circum = get_circum(r)
  return area,circum #n개 리턴 가능

def get_area(r):
  area = 3.14 * r**2
  return area

def get_circum(r):
  circum = 2 * 3.14 * r
  return circum

for i in range(1,6,1):
  area,circum = print_info(i)
  print(f"반지름{i}인 원의 넓이는{area}, 원의 둘레는 {circum}입니다")
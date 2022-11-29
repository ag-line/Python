score = int(input("성적을 입력하시오: "))

#비교할 순서 중요함
if score >= 90:
  print("학점A")
elif score >= 80:
  print("학점B")
elif score >= 70:
  print("학점C")
elif score >= 60:
  print("학점D")
else:
  print("학점F")
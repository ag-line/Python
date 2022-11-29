import random

num = random.randint(1,10)
cnt = 0

print("1번부터 10사이 숫자를 입력하세요")
while True:
  guess = int(input("입력: "))
  cnt += 1
  print(f"{cnt}번째 시도")
  if guess == num:  
    print(f"{num} 정답")
    break
  elif guess < num:
    print("UP")
    continue
  elif guess > num:
    print("DOWN")
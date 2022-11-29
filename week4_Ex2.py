import random

print("동전 던지기 게임을 시작합니다")
#coin = random.randrange(2)
coin = random.randint(0,1)

if coin == 0:
  print(coin)
  print('앞면')
else:
  print(coin)
  print('뒷면')
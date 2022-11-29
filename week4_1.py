print("------------------------------------------")
price = int(input("상품의 가격을 입력하세요: "))
ea = int(input("상품의 개수를 입력하세요: "))
product = int(price * ea)
print("------------------------------------------")
tax = int(product*0.1)
vol = int(product*0.05)
sum = int(product + tax + vol)
print("세전(10%): ",tax)
print(f"봉사료(5%): {vol}")
print("전체가격 = ", sum)
print("------------------------------------------")
in_Money = int(input("지폐를 넣어주세요: "))
print("------------------------------------------")
out_Money = int(in_Money - sum)
print(f"거스름돈: {out_Money}")

if out_Money >= 10000:
  ch_OneM = int((in_Money - sum) // 10000)
  print(f"10000원 지폐의 개수: {ch_OneM}")
if (out_Money-10000* ch_OneM) >= 5000:
  ch_FiveT = int((out_Money - ch_OneM * 10000) // 5000)
  print(f"5000원 지폐의 개수: {ch_FiveT}")
if (out_Money - ch_OneM * 10000 - ch_FiveT*5000) >= 1000:
  ch_OneT = int((out_Money - ch_OneM * 10000 - ch_FiveT*5000) // 1000)
  print(f"1000원 지폐의 개수: {ch_OneT}")
if (out_Money - ch_OneM * 10000 - ch_FiveT*5000 - ch_OneT*1000) >= 500:
  ch_FiveH = int((out_Money - ch_OneM * 10000 - ch_FiveT*5000 - ch_OneT*1000) // 500)
  print(f"500원 동전의 개수: {ch_FiveH}")
if (out_Money - ch_OneM * 10000 - ch_FiveT*5000 - ch_OneT*1000 - ch_FiveH*500) >= 100:
  ch_OneH = int((out_Money - ch_OneM * 10000 - ch_FiveT*5000 - ch_OneT*1000 - ch_FiveH*500) // 100)
  print(f"100원 동전의 개수: {ch_OneH}")
if(out_Money - ch_OneM * 10000 - ch_FiveT*5000 - ch_OneT*1000 - ch_FiveH*500 - ch_OneH*100) >= 50:
  ch_Fifth = int((out_Money - ch_OneM * 10000 - ch_FiveT*5000 - ch_OneT*1000 - ch_FiveH*500 - ch_OneH*100) // 50)
  print(f"50원 동전의 개수: {ch_Fifth}")
  
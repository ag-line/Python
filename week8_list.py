list_num = [10,50,20,100]
print(f"합 {sum(list_num)},최대 {max(list_num)},최소 {min(list_num)}")

#리스트 합병
fruit = ["사과","바나나","포도"]
merge = list_num + fruit
print(merge) #[10, 50, 20, 100, '사과', '바나나', '포도']

#리스트 비교
num1 = [1,3,10,50]
num2 = [59,2,3,5]
print(num1 == num2) #False
print(num1 < num2)  #True

#리스트 복제
number = ["line"]*3
print (number)  #['line', 'line', 'line']

#리스트 얉은 복사
low_copy = num1 
low_copy[2] = "변경"
print(num1)     #low_copy == num1 == [1, 3, '변경', 50]

#리스트 깊은 복사
deep_copy = list(num2)
deep_copy[1] = "변경"
print(num2)       #[59, 2, 3, 5]
print(deep_copy)  #[59, '변경', 3, 5]

#리스트 스라이싱
temp = [00,10,20,30,40,50]
print(temp[1:4])    # 1번부터 3번까지 [10, 20, 30]
print(temp[1:5:2])  # 1번부터 step2주고 4번까지 [10, 30]

print(temp[2:])     # 2번부터 끝까지 [20, 30, 40, 50]
print(temp[:3])     # 처음부터 2번까지 [0, 10, 20]

print("temp[:]",temp[:] ," == ",list(temp))  # 처음부터 끝까지 [0, 10, 20, 30, 40, 50](== 깊은복사)
print(temp[::-1])   # 처음부터 끝까지 step1주고 역순 [50, 40, 30, 20, 10, 0]
print(temp[::-2])   # 처음부터 끝까지 step2주고 역순[50, 30, 10]

#리스트 변경
temp[1:2] = [1,2] 
print(temp)   # 일부 변경 [0, 1, 2, 20, 30, 40, 50]
temp[::2] = [9,9,9,9]
print(temp)   # step씩 끝까지 변경 [9, 1, 9, 20, 9, 40, 9]

#리스트 모두 삭제
temp[:] = []
print(temp) #[]
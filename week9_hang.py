import numpy as np
mat = [[i for i in range(1,6)],[i for i in range(6,11)],[i for i in range(11,16)]]
matT = []
for i in range(len(mat[0])):
  matT_row = []
  for j in range(len(mat)):
    matT_row.append(mat[j][i])
  matT.append(matT_row)

print(f"(len: {len(mat)}) mat : {mat} ")
print(f"(len: {len(matT)}) matT : {matT}")

arr = np.array(mat)
arrT = np.transpose(arr)

print("arr:")
print(arr)
print(np.shape(arr)) #행,열 프린트
print("arrT:")
print(arrT)
print(np.shape(arrT)) #행,열 프린트


oneArr = np.ones(5,dtype=int)
TwoArr = np.ones((5,3),dtype=int)
print(oneArr) # 1 다섯개로 채운 1차원
print(TwoArr) # 1 3개로 채운 2차원 5행3열

zeroArr = np.zeros(5)
print(zeroArr) #0으로 5(size)개


""" 
#text file(6byte) ->w(쓰기모드)
f = open("num.txt","w") #6byte크기를 갖는 파일이 생김
f.write(str(num))
f.close()

f = open("num.txt","r")
buf = f.read()
print(buf,type(buf)) 
"""
#binary파일 ->wb(쓰기), rb(읽기)
f = open("num.bin","wb")
'''
f.write(bytes(num))   
  #(정수)넣으면 0으로 이루어진 객체가 생성 -> \x00 * num번 반복해서 출력됨 
바이트 객체 (문자열 넘김) 출력: b'문자열' <class 'bytes'>
f.write(bytes(b"123")) or f.write(bytes("123".encode()))  
f.write(bytes(b"123456")) 
  # b'123456' <class 'bytes'> 크기 6byte

123456(dec) = (bin) 0001 1110 0010 0100 0000 
  format <bin = (hex)16진 = (dec)10진>
==> 00000001 = x01 = 1 / 1110 0010 = xe2 = 226 / 0100 0000 = @ = 64   //크기: 3byte

'''
#f.write(bytes([1,226,64])) #b' \x01\xe2@ ' <class 'bytes'>
f.write(bytes([91, 160])) #b' [\xa0 ' <class 'bytes'>
f.close

f = open("num.bin","rb")
buf = f.read() 
print(buf,type(buf))
f.close

## byte -> int
  # Create a signed int
i = int.from_bytes(b'[\xa0', byteorder='big', signed=True)
print(i) #23456
  # Use a list of integers 0-255 as a source of byte values
i = int.from_bytes([1,226,64], byteorder='big')
print(i) #123456


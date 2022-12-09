#copy
infile = open("week14_img.jpg","rb")
buf = infile.read()
infile.close()
#paste
outfile = open("week14.jpg","wb")
#outfile.write(buf) #이미지 복사됨
#outfile.write(buf[0:len(buf)//2]) #이미지 처음부터 중간까지 절반만 복사됨
outfile.write(buf[0:len(buf)//2]) #이미지 처음부터 중간까지 절반만 복사됨

outfile.close()
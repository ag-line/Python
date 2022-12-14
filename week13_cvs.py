import csv

""" f =open("Ncode.csv")
data = csv.reader(f)
for row in data:
  print(row)
f.close() 
#['KR', 'Korea', 'Seoul']
['US', 'USA', 'Washington']
['JP', 'Japan', 'Tokyo']
['CN', 'China', 'Beijing']
['RU', 'Rusia', 'Mosow']
"""

f =open("Ncode.csv")
data = csv.reader(f)
print(data,type(data)) 
  #<_csv.reader object at 0x000001ACA5930520> <class '_csv.reader'>
f.close() 

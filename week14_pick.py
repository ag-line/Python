import pickle

gameOpt = {"sound":8, "VideoQ":"High", "Money": 100000, "weaponList":["gun","missile","knife"]}
#write
f = open("week14_game.p","wb")
pickle.dump(gameOpt,f)
f.close()
#read
f = open("week14_game.p","rb")
obj = pickle.load(f)
print(obj,type(obj)) # gameOpt 그대로 출력됨 <class 'dict'>
f.close()

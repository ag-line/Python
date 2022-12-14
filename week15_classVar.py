class TV:
  #class Var = always maked = 공통 데이터
  serial_Num = 0 
  comp = "S"

  #instance var = object make => Var making 
  def __init__(self,channel,vol,on):
    self.channel = channel
    self.vol = vol
    self.on = on
    TV.serial_Num += 1
    self.number = TV.serial_Num

  def show(self):
    print(self.channel, self.vol, self.on, self.number, TV.comp)

mTV1 = TV(11,10,True)
mTV1.show() #11 10 True 1

mTV2 = TV(11,10,True)
mTV2.show() #11 10 True 2

#class Var 접근법
print(TV.comp, mTV1.comp) #S S

class BankAccount:
  bankName = "shinHan"
  def __init__(self):
    self.__balance = 0
  def withdraw(self, amount):
    self.__balance -= amount
    return self.__balance
  def deposit(self, amount):
    self.__balance += amount
    return self.__balance
  def show(self):
    print(BankAccount.bankName, self.__balance)

a = BankAccount()
b = a
a.deposit(100000)
a.show()
# class Var 접근법 : a.bankName, BankAccount.bankName, b.bankName

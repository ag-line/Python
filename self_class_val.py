class joneray:
    def __init__(self, place, money):
        self.__place = place
        self.money = money

    def cost(self):
        if self.__place == "dokyo":
            cost = 1800000
        elif self.__place == "danang":
            cost = 2000000
        return cost

    def addMoney(self, cost):
        addMoney = cost - self.money
        if addMoney < 0:
            print("충분")
        else:
            print(f"{addMoney}원이 더 필요합니다")

    def show(self, cost):
        print(f"{self.__place} 예상여행비용: {cost}")


a = joneray("dokyo", 1000000)
cost = a.cost()
a.show(cost)
a.addMoney(cost)

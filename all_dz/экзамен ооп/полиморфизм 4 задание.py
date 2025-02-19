class All:
    def work(self):
        raise NotImplementedError("Метод должен быть переопределён в дочернем классе")

class Peon(All):
    def work(self):
        print("Собирает золото")

class Knight(All):
    def work(self):
        print("Сражается с врагами")

def daily_work(all):
    print(all.work())

peon = Peon()
knight = Knight()


daily_work(peon)   # Вывод: Собирает золото
daily_work(knight) # Вывод: Сражается с врагами
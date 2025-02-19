class Peon:

    def work(self):
        return "Собирает золото"

class Knight:

    def work(self):
        return "Сражается с врагами"


def daily_work(hero):
    print(hero.work())


peon = Peon()
knight = Knight()

daily_work(peon)   # Вывод: Собирает золото
daily_work(knight) # Вывод: Сражается с врагами
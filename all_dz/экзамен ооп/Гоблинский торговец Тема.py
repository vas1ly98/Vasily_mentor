class GoblinTrader:
    def __init__(self, gold):
        self.gold = gold

    def buy_item(self, item_name, item_price):
        if self.gold - item_price >= 0:
            self.gold -= item_price
            print(f'Куплен, {item_name}')
        else:
            print('нету денег')



trader = GoblinTrader(200)
trader.buy_item("Свиток скорости", 150)  # Вывод: Куплен Свиток скорости
trader.buy_item("Книга заклинаний", 100)  # Вывод: Недостаточно золота!
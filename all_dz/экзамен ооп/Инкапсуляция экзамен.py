class GoblinBank:
    def __init__(self, gold):
        self.__gold = gold
        if gold < 0:
            raise ZeroDivisionError("Баланс отрицательный")


    def get_gold(self):
        return self.__gold

    def deposit_gold(self, amount):
        self.amount = amount
        if self.amount > 0:
            self.__gold += amount
        print(f'Добавлено {amount} золота. Текущий баланс: {self.__gold}')

    def withdraw_gold(self, amount):
        self.amount = amount
        if self.__gold - amount > 0:
            print(f'Вывод: Снято {amount} золота. Текущий баланс: {self.__gold}')
        else:
            print('Вывод: Недостаточно золота!')

bank = GoblinBank(100)

print(bank.get_gold())  # Вывод: 100
bank.deposit_gold(50)   # Вывод: Добавлено 50 золота. Текущий баланс: 150
bank.withdraw_gold(30)  # Вывод: Снято 30 золота. Текущий баланс: 120
bank.withdraw_gold(200) # Вывод: Недостаточно золота!
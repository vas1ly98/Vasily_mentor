class GoblinBank:

    def __init__(self, gold):
        self.__gold = gold
        if self.__gold < 0:
            raise 'ошибка'

    def get_gold(self):
        return self.__gold

    def deposit_gold(self, amount):
        if amount > 0:
            self.__gold += amount
        print(f'Добавлено {amount} золота. Текущий баланс: {self.__gold}')

    def withdraw_gold(self, amount):
        if self.__gold - amount > 0:
            self.__gold - amount
            print(f'Снято {amount} золота. Текущий баланс: {self.__gold}')
        else:
            print("Недостаточно золота!")

bank = GoblinBank(100)

print(bank.get_gold())

bank.deposit_gold(50)
bank.withdraw_gold(30)
bank.withdraw_gold(200)


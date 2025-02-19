class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def is_positive(x):
        return x > 0


# Использование статических методов
print(MathUtils.add(5, 7))  # Вывод: 12
print(MathUtils.multiply(3, 4))  # Вывод: 12


class Convector:
    @staticmethod
    def usd_to_eur(amount):
        return  amount * 0.8

    @staticmethod
    def eur_to_usd(amount):
        return amount * 1,18

print(Convector.usd_to_eur(1234))

print()



class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Защищенный атрибут

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Сумма депозита должна быть положительной.")


    def withdraw(self, amount):
        if 0 < amount <= self._balance :
            self._balance -= amount
        else:
            print("Недостаточно средств или некорректная сумма.")

    def get_balance(self):
        return self._balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(2000)
print(account.get_balance())
"""Мы можем обратиться к защищенному атрибуту напрямую, но это не рекомендуется"""
print(account._balance)  # Вывод: 1500 (но лучше использовать account.get_balance())

account._balance = -1000 #можем изменить напрямую, но это плохо
print(account.get_balance()) #вывод -1000, что недопустимо
account.withdraw(100)
print(account.get_balance()) #вывод -1100, что недопустимо
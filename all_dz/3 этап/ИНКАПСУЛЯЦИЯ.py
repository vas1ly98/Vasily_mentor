class Product:
    def __init__(self, name, price):
        self.name = name  # Открытый атрибут
        self.__price = price  # Приватный атрибут

    # Геттер для получения значения атрибута price
    @property
    def price(self):
        return self.__price

    # Сеттер для изменения значения атрибута price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной!")
        self.__price = value

# Использование
product = Product("Ноутбук", 50000)

# Доступ к открытому атрибуту
print(product.name)  # Ноутбук

# Попытка получить доступ к приватному атрибуту (будет ошибка)
# print(product.__price)

# Работа с приватным атрибутом через геттер и сеттер
print(product.price)  # 50000
product.price = 45000  # Изменение цены
print(product.price)  # 45000
print()

# Попытка установить некорректную цену
# product.price = -100  # ValueError: Цена не может быть отрицательной!


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Открытый атрибут
        self.__balance = balance  # Приватный атрибут

    # Геттер для получения баланса
    @property
    def balance(self):
        return self.__balance

    # Сеттер для депозита
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} добавлено. Новый баланс: {self.__balance}")
        else:
            print("Сумма должна быть положительной!")

    # Метод для снятия денег
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} снято. Новый баланс: {self.__balance}")
        else:
            print("Недостаточно средств или некорректная сумма.")

# Использование
account = BankAccount("Иван", 1000)
print(account.balance)  # 1000
account.deposit(500)  # 500 добавлено. Новый баланс: 1500
account.withdraw(200)  # 200 снято. Новый баланс: 1300
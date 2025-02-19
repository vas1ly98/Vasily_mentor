


class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages


    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def pages(self):  # Геттер главное запомнить без геттера ты не создашь сеттер
        return self._pages

    @pages.setter
    def pages(self, new_pages):
        if new_pages < 0:
            print("Башкой подумай как страницы могут быть отрицательными")
        else:
            self._pages = new_pages



class BankAccount:
    def __init__(self, account_number:str, balance:float):
        self._account_number = account_number
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if self._balance - new_balance < self._balance:
            print('снимать монеты нельзя')
        if new_balance < 0:
            print('баланс отрицательный')
        else:
            self._balance += new_balance

    def withdraw(self, amount):
        if 0 < amount < self._balance:
            self._balance -= amount
        else:
            print("Недостаточно средств или некорректная сумма.")

bankAccount = BankAccount("123213",  384)
print(bankAccount.balance)  # Вывод: Мастер и Маргарита
bankAccount.balance = -100000  # Вывод: Количество страниц не может быть отрицательным.
print(bankAccount.balance)

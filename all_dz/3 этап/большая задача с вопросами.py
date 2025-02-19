class Account:
    def __init__(self, name, balance):
        # Проверка, что баланс не отрицательный
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным!")   # это короче тот момент на котором код оборвется если будет такая ошибка
        self.name = name
        self.balance = balance #тут мы просто присваиваем имена атрибуты класса

    def deposit(self, amount):     #тут идут методы класса
        if amount < 0:
            raise ValueError("Сумма депозита не может быть отрицательной!")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Сумма снятия не может быть отрицательной!")
        if self.balance - amount < 0:
            raise ValueError("Недостаточно средств на счете!")
        self.balance -= amount

    def get_balance(self):
        return self.balance

class SavingAccount(Account): #тут новый класс наследует все что есть у старого Account
    def __init__(self, name, balance, interest_rate ):
        self.interest_rate = interest_rate  #тут добавляем параметры
        super().__init__(name, balance) # тут короче берем с помощью методу super наследуем  атрибуты класса name, balance без self

    def apply_interest(self):
        # Применение процента к балансу
        self.balance += self.balance * (self.interest_rate / 100)

    def withdraw(self, amount):
        if self.balance - amount < 100:
            raise ValueError("остаток должен быть больше 100") # суть такая что мы сюда добавили дополнительную проверку к родительскому методу
        super().withdraw(amount) # тут мы берем и вызываем в этой части кода родительский метод, просто с дополнительной проверкой которая написана выше
# вызываем его с передачей аргумента amount
try:
    withdraw(200)
except ValueError as e:
    print(f"Ошибка: {e}")
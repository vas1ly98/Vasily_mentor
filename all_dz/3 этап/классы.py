class Book:
    def __init__(self, title, author, pages):
        self.title = title  # Атрибут title для объекта
        self.author = author # Атрибут author для объекта
        self.pages = pages  # Атрибут pages  для объекта

# Создаем объект класса Human
Book1 = Book("supergood", 'petr', "2312")
Book2 = Book("zxc", 'vasya', "женский")


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):# тут просто всегда будет self?
        print(f'I am an animal, my name is {self.name} and my age {self.age}') # почему тут без селфа ниче не работает

miniAnimal = Animal('vasya', 22)


miniAnimal.speak()


miniAnimal.age = 124
miniAnimal.name = "xoz9in"

miniAnimal.speak()

class Animal:
    def __init__(self, name):
        print("Animal init called")
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        print("Dog init called")
        super().__init__(name)  # Вызов __init__ родителя
        self.breed = breed

dog = Dog("Rex", "Bulldog")
print(dog.name)  # Rex
print(dog.breed)  # Bulldo




class Account:
    def __init__(self, name, balance):
        # Проверка, что баланс не отрицательный
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным!")
        self.name = name
        self.balance = balance

    def deposit(self, amount):
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

class SavingAccount(Account):
    def __init__(self, name, balance, interest_rate ):
        self.interest_rate = interest_rate
        super().__init__(name, balance) # тут короче берем

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
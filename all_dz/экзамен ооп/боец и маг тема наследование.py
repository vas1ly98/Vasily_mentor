class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health


    def take_damage(self, damage):
       self.health - damage
       print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")

class Warrior(Hero):
    def attack(self):
        return 'нанес 20 урона мечом'


class Mage(Hero):
    def attack(self):
        return 'нанес 15 урона заклинанием'




warrior = Warrior("Тралл", 120)
mage = Mage("Джайна", 80)

print(warrior.attack())  # Вывод: Нанёс 20 урона мечом
print(mage.attack())     # Вывод: Нанёс 15 урона заклинанием
print(warrior.take_damage(15))

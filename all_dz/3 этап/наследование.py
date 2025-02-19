# Базовый класс
class Hero:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"{self.name} бежит")

    def fight(self):
        print(f"{self.name} борется с врагом")

# Дочерний класс
class SpiderMan(Hero):  # Наследуем класс Hero
    def shoot_web(self):
        print(f"{self.name} выпускает паутину")

# Создаём героя
hero = SpiderMan("Человек-Паук")
hero.run()  # Человек-Паук бежит
hero.fight()  # Человек-Паук борется с врагом
hero.shoot_web()  # Человек-Паук выпускает паутину

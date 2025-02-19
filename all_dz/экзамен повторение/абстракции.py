from abc import ABC, abstractmethod

class Artifact(ABC):

    @abstractmethod
    def activate(self):
        pass

class DamageArtifact:

    def activate(self):
        return "Нанесено 30 урона врагу"

class HealingArtifact:

    def activate(self):
        return "Восстановлено 50 здоровья"

heal_artifact = HealingArtifact()
damage_artifact = DamageArtifact()

print(heal_artifact.activate())  # Вывод: Восстановлено 50 здоровья
print(damage_artifact.activate()) # Вывод: Нанесено 30 урона врагу













from abc import ABC, abstractmethod #что такое импорт?

# Абстрактный класс
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass
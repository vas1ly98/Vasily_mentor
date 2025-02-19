from abc import ABC, abstractmethod #что такое импорт?

# Абстрактный класс
class Artifact(ABC):
    @abstractmethod
    def activate(self):
        pass



class HealingArtifact(Artifact):

    def activate(self):
        return "Восстановлено 50 здоровья"

class DamageArtifact(Artifact):

    def activate(self):
        return "Нанесено 30 урона врагу"

heal_artifact = HealingArtifact()
damage_artifact = DamageArtifact()

print(heal_artifact.activate())  # Вывод: Восстановлено 50 здоровья
print(damage_artifact.activate()) # Вывод: Нанесено 30 урона врагу




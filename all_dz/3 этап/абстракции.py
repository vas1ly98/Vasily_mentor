from abc import ABC, abstractmethod #что такое импорт?

# Абстрактный класс
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        return "Рисуем круг"

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        return "Рисуем прямоугольник"

    def area(self):
        return self.width * self.height


### **Использование абстракции:**


shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(shape.draw())
    print("Площадь:", shape.area())

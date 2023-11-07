class Quadrilateral:
    def __init__(self, width, height=None):
        if height is None:
            height = width
        self.width = width
        self.height = height
    def __str__(self):
        if self.width == self.height:
            return f"Куб размером {self.width}х{self.height}"
        else:
            return f"Прямоугольник размером {self.width}х{self.height}"
    def __bool__(self):
        return self.width == self.height
# Пример использования
# Создание объекта Quadrilateral с одним аргументом
quad1 = Quadrilateral(10)
print(quad1)       # Вывод: Куб размером 10х10
print(bool(quad1)) # Вывод: True
# Создание объекта Quadrilateral с двумя аргументами
quad2 = Quadrilateral(3, 5)
print(quad2)       # Вывод: Прямоугольник размером 3х5
print(bool(quad2)) # Вывод: False
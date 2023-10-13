class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        # Вычисляем периметр треугольника
        p = (1 / 2) * (self.a + self.b + self.c)
        return (f'(P = {self.a} + {self.b} + {self.c}) = {p}')

    def area(self):
        # Вычисляем полупериметр треугольника
        p = (1 / 2) * (self.a + self.b + self.c)
        # Вычисляем площадь треугольника по формуле Герона
        s = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return (f'S = sqrt({p}({p}-{self.a})({p}-{self.b})({p}-{self.c})) = {s}')


# Создаем объект класса Triangle с заданными длинами сторон
triangle = Triangle(5, 7, 9)

# Вызываем методы для вычисления периметра и площади треугольника
perimeter_result = triangle.perimeter()
area_result = triangle.area()

# Выводим результаты
print(perimeter_result)
print(area_result)

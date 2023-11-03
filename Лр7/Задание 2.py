class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def c(self):
        return (self.a ** 2) - 1.7 * self.b

# Пример использования класса A
obj = A(56, 86)  # Создаем объект класса A с a=3 и b=2
result = obj.c  # Вычисляем значение свойства c
print(result)  # Выводим результат
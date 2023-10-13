class Counter:
    def __init__(self, start_value=0):
        self.value = start_value

    def start_from(self, start_value=0):
        self.value = start_value

    def increment(self):
        self.value += 1

    def display(self):
        print(f"Текущее значение счетчика = {self.value}")

    def reset(self):
        self.value = 0

# Пример использования класса Counter:
counter = Counter()  # Создаем экземпляр счетчика с начальным значением 0
counter.display()  # Выводит "Текущее значение счетчика = 0"
counter.increment()  # Увеличиваем счетчик на 1
counter.display()  # Выводит "Текущее значение счетчика = 1"
counter.start_from(10)  # Устанавливаем начальное значение 10
counter.display()  # Выводит "Текущее значение счетчика = 10"
counter.reset()  # Обнуляем счетчик
counter.display()  # Выводит "Текущее значение счетчика = 0"
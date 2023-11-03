class Phone:
    def __init__(self, last_name, first_name, patronymic, address, number, local_call_time, long_distance_call_time):
        self._last_name = last_name
        self._first_name = first_name
        self._patronymic = patronymic
        self._address = address
        self._number = number
        self._local_call_time = local_call_time
        self._long_distance_call_time = long_distance_call_time

    @property
    def local_call_time(self):
        return self._local_call_time

    @local_call_time.setter
    def local_call_time(self, value):
        if value >= 0:
            self._local_call_time = value
        else:
            raise ValueError("Время внутригородских разговоров не может быть отрицательным")

    @property
    def long_distance_call_time(self):
        return self._long_distance_call_time

    @long_distance_call_time.setter
    def long_distance_call_time(self, value):
        if value >= 0:
            self._long_distance_call_time = value
        else:
            raise ValueError("Время междугородних разговоров не может быть отрицательным")

# Пример использования класса Phone
if __name__ == "__main__":
    phone = Phone("Иванов", "Иван", "Иванович", "ул. Ленина, 123", "123456789", 100, 50)
    print(f"Фамилия: {phone._last_name}")
    print(f"Имя: {phone._first_name}")
    print(f"Отчество: {phone._patronymic}")
    print(f"Адрес: {phone._address}")
    print(f"Номер: {phone._number}")
    print(f"Время внутригородских разговоров: {phone.local_call_time} минут")
    print(f"Время междугородних разговоров: {phone.long_distance_call_time} минут")
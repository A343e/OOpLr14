class Apartment:
    def __init__(self, room_count, residents_count):
        self.room_count = room_count
        self.residents_count = residents_count

    @property
    def room_count(self):
        return self._room_count

    @room_count.setter
    def room_count(self, value):
        self._room_count = value

    @property
    def residents_count(self):
        return self._residents_count

    @residents_count.setter
    def residents_count(self, value):
        self._residents_count = value


class House:
    def __init__(self):
        self.apartments = []

    def add_apartment(self, apartment):
        self.apartments.append(apartment)

    def sort_apartments_by_room_count(self):
        self.apartments.sort(key=lambda x: x.room_count)

    def find_apartment_by_residents_count(self, min_count, max_count):
        result = []
        for apartment in self.apartments:
            if min_count <= apartment.residents_count <= max_count:
                result.append(apartment)
        return result


# Создание объектов квартир и добавление их в список
house = House()
house.add_apartment(Apartment(3, 4))
house.add_apartment(Apartment(2, 2))
house.add_apartment(Apartment(4, 3))
house.add_apartment(Apartment(1, 1))

# Сортировка квартир по количеству комнат
house.sort_apartments_by_room_count()

# Поиск квартир в заданном диапазоне числа проживающих
min_residents = 2
max_residents = 4
result = house.find_apartment_by_residents_count(min_residents, max_residents)
print(f"Квартиры с числом проживающих от {min_residents} до {max_residents}:")
for apartment in result:
    print(f"Количество комнат: {apartment.room_count}, Количество проживающих: {apartment.residents_count}")
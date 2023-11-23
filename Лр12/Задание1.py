
class City:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


class Building:
    def __init__(self, street_name, house_number, area, base_monthly_payment):
        self.street_name = street_name
        self.__house_number = house_number
        self.__area = area
        self.__base_monthly_payment = base_monthly_payment

    @property
    def street_name(self):
        return self.__street_name

    @street_name.setter
    def street_name(self, value):
        self.__street_name = value

    @property
    def house_number(self):
        return self.__house_number

    @house_number.setter
    def house_number(self, value):
        self.__house_number = value

    @property
    def area(self):
        return self.__area

    @property
    def base_monthly_payment(self):
        return self.__base_monthly_payment

    @base_monthly_payment.setter
    def base_monthly_payment(self, value):
        self.__base_monthly_payment = value


class Room:
    def __init__(self, number, area):
        self.number = number
        self.__area = area

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        self.__area = value

    def calculate_monthly_payment(self):
        pass


class Apartment(Room):
    def __init__(self, number, area, tenants):
        super().__init__(number, area)
        self.tenants = tenants

    @property
    def tenants(self):
        return self.__tenants

    @tenants.setter
    def tenants(self, value):
        self.__tenants = value

    def calculate_monthly_payment(self):
        try:
            if len(self.__tenants) == 0:
                raise ValueError("No tenants in the apartment")
            else:
                return self.area * 10  # for example
        except ValueError as e:
            print(e)


class Office(Room):
    def __init__(self, number, area, company_name, activity_type):
        super().__init__(number, area)
        self.__company_name = company_name
        self.__activity_type = activity_type

    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, value):
        self.__company_name = value

    @property
    def activity_type(self):
        return self.__activity_type

    @activity_type.setter
    def activity_type(self, value):
        self.__activity_type = value

    def calculate_monthly_payment(self):
        try:
            return self.area * 20
        except Exception as e:
            print(e)
# Создаем объекты классов
city = City("Минск")
building = Building("ул. Немига", 3, 3000, 20)
apartment = Apartment(2, 50, ["Олег Олегович", "Никита Викторович"])
office = Office(3, 200, "ООО 'Кофейня Чикипики'", "Производство")

# Устанавливаем значения свойств
city.name = "Брест"
building.street_name = "ул. Есенина"
apartment.number = 3
office.company_name = "ООО 'Чикибабони'"

# Получаем значения свойств
print(city.name)
print(building.street_name)
print(apartment.number)
print(office.company_name)

# Вызываем методы
try:
    print(apartment.calculate_monthly_payment())
except ValueError as e:
    print(e)

try:
    print(office.calculate_monthly_payment())
except Exception as e:
    print(e)
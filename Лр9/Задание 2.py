class InternetShop:
    def __init__(self, shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, customer_name):
        self.shop_name = shop_name
        self.product_name = product_name
        self.country_of_origin = country_of_origin
        self.payment_method = payment_method
        self.purchase_amount = purchase_amount
        self.sale_date = sale_date
        self.customer_name = customer_name

    def __str__(self):
        return f"Интернет-магазин: {self.shop_name}\nТовар: {self.product_name}\nСтрана производитель: {self.country_of_origin}\n" \
               f"Вид оплаты: {self.payment_method}\nСумма покупки: {self.purchase_amount}\nДата продажи: {self.sale_date}\n" \
               f"Покупатель: {self.customer_name}"


class LivingRoomFurniture(InternetShop):
    def __init__(self, shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, customer_name, furniture_name, price, furniture_type, manufacturer):
        super().__init__(shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, customer_name)
        self.furniture_name = furniture_name
        self.price = price
        self.furniture_type = furniture_type
        self.manufacturer = manufacturer

    def __str__(self):
        return super().__str__() + f"\nТип мебели для гостиных: {self.furniture_type}\nНазвание мебели: {self.furniture_name}\n" \
                                   f"Цена: {self.price}\nПроизводитель: {self.manufacturer}"


class KitchenFurniture(InternetShop):
    def __init__(self, shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, customer_name, furniture_name, price, length, height, width, material):
        super().__init__(shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, customer_name)
        self.furniture_name = furniture_name
        self.price = price
        self.length = length
        self.height = height
        self.width = width
        self.material = material

    def __str__(self):
        return super().__str__() + f"\nТип мебели для кухни\nНазвание мебели: {self.furniture_name}\nЦена: {self.price}\n" \
                                   f"Длина: {self.length} см\nВысота: {self.height} см\nШирина: {self.width} см\n" \
                                   f"Материал: {self.material}"


class BathroomFurniture(InternetShop):
    def __init__(self, shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, customer_name, furniture_name, price):
        super().__init__(shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, customer_name)
        self.furniture_name = furniture_name
        self.price = price

    def __str__(self):
        return super().__str__() + f"\nТип мебели для ванн\nНазвание мебели: {self.furniture_name}\nЦена: {self.price}"


# Пример использования
living_room_furniture = LivingRoomFurniture("Мебельный магазин", "Диван", "Италия", "Кредитная карта", 1500, "2023-11-08", "Иван Иванов",
                                           "Кожаный диван", 800, "Диван", "Икеа")
kitchen_furniture = KitchenFurniture("Мебельный магазин", "Кухонный стол", "Германия", "Наличные", 350, "2023-11-09", "Мария Сидорова",
                                   "Дубовый стол", 350, 120, 75, 80, "Дуб")
bathroom_furniture = BathroomFurniture("Мебельный магазин", "Зеркало", "Китай", "Банковская карта", 100, "2023-11-10", "Петр Петров",
                                    "Зеркало с подсветкой", 100)

print(living_room_furniture)
print("\n" + "-" * 50 + "\n")
print(kitchen_furniture)
print("\n" + "-" * 50 + "\n")
print(bathroom_furniture)

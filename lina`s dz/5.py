class Unit:
    def __init__(self, name="упаковка", volume=1, material="пластик", suitable_for_liquid=False):
        self.name = name
        self.volume = volume
        self.material = material
        self.suitable_for_liquid = suitable_for_liquid

class Food:
    def __init__(self, name, quantity=0, unit=Unit()):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def state(self):
        return "не определено"

class Sugar(Food):
    def state(self):
        return "сыпучее"

class Juice(Food):
    def state(self):
        return "жидкость"

class Bread(Food):
    def state(self):
        return "твердое"

class Stock:
    def __init__(self):
        self.stock = {}

    def append(self, food, quantity):
        if food.name in self.stock:
            self.stock[food.name].quantity += quantity
        else:
            self.stock[food.name] = food
            self.stock[food.name].quantity = quantity

    def bought(self, food_name, quantity):
        if food_name in self.stock:
            if self.stock[food_name].quantity >= quantity:
                self.stock[food_name].quantity -= quantity
                if self.stock[food_name].quantity == 0:
                    del self.stock[food_name]
            else:
                print(f"Недостаточно товара {food_name} на складе.")
        else:
            print(f"Товара {food_name} нет на складе.")

    def remove(self, food_name):
        if food_name in self.stock:
            del self.stock[food_name]
        else:
            print(f"Товара {food_name} нет на складе.")

    def __getitem__(self, food_name):
        if food_name in self.stock:
            return f"Остаток {food_name}: {self.stock[food_name].quantity} {self.stock[food_name].unit.name}"
        else:
            return f"Товара {food_name} нет на складе."

    def __str__(self):
        stock_info = "Содержимое склада:\n"
        for food_name, food in self.stock.items():
            stock_info += f"{food_name}: {food.quantity} {food.unit.name}, состояние: {food.state()}\n"
        return stock_info

# 2. Создание списка элементов класса Unit
units = [
    Unit("упаковка", 1, "пластик", False),
    Unit("пачка", 0.5, "картон", False),
    Unit("бутылка", 1, "стекло", True),
    Unit("банка", 0.33, "жесть", True)
]

# 4. Создание экземпляров классов конкретных товаров
sugar = Sugar("Сахар", 10, units[0])
juice = Juice("Сок", 20, units[2])
bread = Bread("Хлеб", 15, units[1])

# 5. Создание экземпляра класса Stock
stock = Stock()

# 6. Добавление товаров на склад
stock.append(sugar, 10)
stock.append(juice, 20)
stock.append(bread, 15)

# Вывод содержимого склада
print(stock)

# Проверка метода __getitem__
print(stock["Сахар"])
print(stock["Сок"])
print(stock["Хлеб"])

# Уменьшение количества товара (покупка)
stock.bought("Сахар", 5)
stock.bought("Сок", 10)
stock.bought("Хлеб", 5)

# Вывод содержимого склада после покупки
print(stock)

# Удаление товара со склада
stock.remove("Хлеб")

# Вывод содержимого склада после удаления
print(stock)
class Phone:
    # 1. Переменные класса number, model и weight
    def __init__(self, number=None, model=None, weight=None):
        self.number = number
        self.model = model
        self.weight = weight

    # 4.1 Метод receiveCall с одним параметром
    def receiveCall(self, name):
        print(f"Звонит {name}")

    # 4.2 Метод getNumber
    def getNumber(self):
        return self.number

    # 8. Перегруженный метод receiveCall с двумя параметрами
    def receiveCall(self, name, caller_number):
        print(f"Звонит {name} с номера {caller_number}")

    # 9. Метод sendMessage с аргументами переменной длины
    def sendMessage(self, *numbers):
        print("Номера телефонов, которым будет отправлено сообщение:")
        for number in numbers:
            print(number)

# 2. Создание трех экземпляров класса Phone
phone1 = Phone("7-561-354-40-86", "iPhone 16", 174)
phone2 = Phone("7-318-956-80-01", "Samsung Galaxy S20", 169)
phone3 = Phone("7-365-034-93-16", "realme 12", 151)
phone4 = Phone()

# 3. Вывод значений переменных по умолчанию
print(f"Phone 1: Number={phone1.number}, Model={phone1.model}, Weight={phone1.weight}")
print(f"Phone 2: Number={phone2.number}, Model={phone2.model}, Weight={phone2.weight}")
print(f"Phone 3: Number={phone3.number}, Model={phone3.model}, Weight={phone3.weight}")
print(f"Phone 4: Number={phone4.number}, Model={phone4.model}, Weight={phone4.weight}\n")

# 4. Вызов методов для каждого объекта
phone1.receiveCall("Иван", "7-561-354-40-86")
print(f"Номер телефона: {phone1.getNumber()}\n")

phone2.receiveCall("Мария", "7-318-956-80-01")
print(f"Номер телефона: {phone2.getNumber()}\n")

phone3.receiveCall("Алексей", "7-365-034-93-16")
print(f"Номер телефона: {phone3.getNumber()}\n")

# 9. Вызов метода sendMessage
phone1.sendMessage("7-561-354-40-86", "7-318-956-80-01", "7-365-034-93-16")
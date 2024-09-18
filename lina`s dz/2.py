import random

class Person:
    # 1. Переменная класса status
    status = 'человек'

    # 2. Конструктор класса
    def __init__(self, fullName=None, age=None):
        self.fullName = fullName
        self.age = age

class Operator(Person):
    def __init__(self, operator_id):
        super().__init__(fullName=f"Оператор {operator_id}")
        self.speaks = False

    def talk(self):
        self.speaks = True

    def stop(self):
        self.speaks = False

# 3. Создание списка операторов call-центра
operators = [Operator(i) for i in range(1, 9)]  # Создаем 5 операторов с ID от 1 до 9

# 4. Случайный выбор операторов на линии и в ожидании
for operator in operators:
    if random.choice([True, False]):
        operator.talk()
    else:
        operator.stop()

# Вывод информации о каждом операторе
for operator in operators:
    if operator.speaks:
        print(f"{operator.fullName} говорит")
    else:
        print(f"{operator.fullName} ожидает")


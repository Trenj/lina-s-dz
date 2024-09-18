class Person:
    # 1. Переменная класса status
    status = 'человек'

    # 2. Конструктор класса
    def __init__(self, fullName=None, age=None):
        self.fullName = fullName
        self.age = age

# 3. Создание двух объектов класса Person
person1 = Person()
person2 = Person("Иван Иванов", 30)

# 4. Задание значений переменных для первого объекта
person1.fullName = "Петр Петров"
person1.age = 25

# 5. Вывод имени и возраста двух объектов на консоль
print(f"Первый объект: {person1.fullName}, {person1.age} лет\n")
print(f"Второй объект: {person2.fullName}, {person2.age} лет\n")
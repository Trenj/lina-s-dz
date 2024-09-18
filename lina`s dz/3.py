import random

class Person:
    # 1. Переменная класса status
    status = 'человек'

    # 2. Конструктор класса
    def __init__(self, fullName=None, age=None, income=None):
        self.fullName = fullName
        self.age = age
        self._income = income

    # 4. Метод setincome(value)
    def setincome(self, value=None):
        if value is None:
            self._income = random.randint(1000, 5000)  # Случайное значение дохода
        else:
            self._income = value

    # 5. Метод getincome()
    def getincome(self):
        print(f"Доход {self.fullName}: {self._income} руб.")

class Student(Person):
    # 3. Переопределение переменной класса status
    status = 'студент'

    def __init__(self, fullName, age, higherSchool, group, averageMark, income=None):
        super().__init__(fullName, age, income)
        self.higherSchool = higherSchool
        self.group = group
        self.averageMark = averageMark

    # 6. Переопределение метода setincome()
    def setincome(self):
        if self.averageMark > 4.5:
            self._income = 2000
        elif self.averageMark > 3.5:
            self._income = 1600
        else:
            self._income = 0

# 7. Создание списка объектов класса Person и Student
people = [
    Person("Иван Иванов", 30, 3500),
    Person("Петр Коптелов", 25),
    Student("Пабло Сабаев", 20, "ОмГМУ", "123", 4.8),
    Student("Анна Лебедева", 22, "МГУ", "456", 3.7),
    Student("Корней Спицын", 19, "ЮУрГУ", "789", 3.9)
]

# Вызов метода getincome() для каждого элемента массива
for person in people:
    if isinstance(person, Student):
        person.setincome()
    else:
        person.setincome()
        
    person.getincome()
    print(f"Имя: {person.fullName}, Статус: {person.status}, Доход: {person._income} руб.")
    if isinstance(person, Student):
        print(f"Средняя оценка: {person.averageMark}\n")
    else:
        print("")
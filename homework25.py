'================= Umar ================'

# 1. Абстрактный транспорт
# Создай абстрактный класс Transport с абстрактным методом move(). Реализуй два
# класса Car и Plane, которые наследуются от Transport и реализуют метод move() по-
# своему.
# Пример вывода:
# Car is moving on the road
# Plane is flying in the sky

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        ... 

class Car(Transport):
    def move(self):
        print('машина движется по дороге')

class Plane(Transport):
    def move(self):
        print('самолет летит в небе')

objects = [Car(), Plane()]

for obj in objects:
    obj.move()


# 2. Платёжная система
# Создай абстрактный класс PaymentMethod с методом pay(amount). Сделай классы
# CreditCard и PayPal, реализующие этот метод с выводом способа оплаты и суммы.
# Пример вывода:
# Оплата 1000 через Credit Card
# Оплата 500 через PayPal

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        ...

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f'Оплата {amount} через Credit Card')
    
class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f'Оплата {amount} через PayPal')

objects = [CreditCard(), PayPal()]

for obj in objects:
    obj.pay(500)

        
# 3. Фигуры и площадь
# Создай абстрактный класс Shape с методом area(). Реализуй классы Circle и Rectangle с
# соответствующим вычислением площади.
# Пример вывода:
# Площадь круга: 78.5
# Площадь прямоугольника: 200

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f'Площадь круга: {round(math.pi * self.radius**2, 2)}')

class Rectengles(Shape):
    def __init__(self, withhd, height):
        self.withd = withhd
        self.height = height

    def area(self):
        print(f'Площадь прямоугольника: {self.withd * self.height}')

obj_Circle = Circle(50)
obj_Circle.area()
obj_Rectengl = Rectengles(20, 40)
obj_Rectengl.area()

# 4. Устройства вывода
# Определи абстрактный класс OutputDevice с методом display(text). Создай Monitor и
# Printer, которые выводят текст по-разному (например, просто через print, но с
# разными префиксами).
# Пример вывода:
# [Monitor] Hello, world!
# [Printer] Hello, world!

from abc import ABC, abstractmethod

class OutputDevice(ABC):
    @abstractmethod
    def display(self,text):
        ...

class Monitor(OutputDevice):
    def display(self, text):
        print(f'[Monitor] {text}')

class Printer(OutputDevice):
    def display(self, text):
        print(f'[Printer] {text}')

obj_M = Monitor()
obj_M.display('Hello, world!')
obj_P = Printer()
obj_P.display('Hello, world!')


# 5. Абстрактный животный класс
# Создай абстрактный класс Animal с методом make_sound(). Создай два класса Dog и
# Cat, которые реализуют этот метод (выводят «Гав!» и «Мяу!» соответственно).
# Пример вывода:

# Гав!
# Мяу!

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        ...

class Dog(Animal):
    def make_sound(self):
        print('Гав!')
    
class Cat(Animal):
    def make_sound(self):
        print('Мяу!')

animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()

# 6. Абстрактный работник
# Определи класс Employee с методом calculate_salary(). Сделай Developer и Manager,
# возвращающие зарплату с разными расчётами (фикс + бонус, почасовая и т.п.).
# Пример вывода:
# Зарплата разработчика: 5000
# Зарплата менеджера: 7000

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        ...

class Developer(Employee):
    def __init__(self, fixed_salary, bonus):
        self.fixed_salary = fixed_salary
        self.bonus = bonus
    
    def calculate_salary(self):
        print(f'Зарплата разработчика: {self.fixed_salary + self.bonus}')
    
class Manager(Employee):
    def __init__(self, hourly_salary, watch):
        self.hourly_salary = hourly_salary
        self.watch = watch

    def calculate_salary(self):
        print(f'Зарплата менеджера: {self.hourly_salary * self.watch}')

objects = [Developer(5000, 500), Manager(30, 200)]

for obj in objects:
    obj.calculate_salary()



# 7. Интерфейс базы данных
# Создай абстрактный класс Database с методами connect() и disconnect(). Реализуй
# классы MySQLDatabase и PostgreSQLDatabase, которые выводят информацию о
# подключении/отключении.
# Пример вывода:
# Подключение к MySQL
# Отключение от MySQL
# Подключение к PostgreSQL
# Отключение от PostgreSQL

from abc import ABC, abstractmethod

class Datebase(ABC):
    @abstractmethod
    def connect(self):
        ...
    @abstractmethod
    def disconnect(self):
        ...
    
class MySQLDatabase(Datebase):
    def connect(self):
        print('Подключение к MySQL')
    
    def disconnect(self):
        print('Отключение от MySQL')

class PostSQLDatabase(Datebase):
    def connect(self):
        print('Подключение к PostgreSQL')
    
    def disconnect(self):
        print('Отключение от PostgreSQL')
    
objects = [MySQLDatabase(), PostSQLDatabase()]

for obj in objects:
    obj.connect()
    obj.disconnect()

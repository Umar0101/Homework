'=================  Umar  =================='

# Таски по полиморфизму в Python
# Таск 1. Универсальный принтер
# Описание:
# Создай базовый класс `Document`, у которого есть метод `print_info()`.
# Создай два подкласса — `PDFDocument` и `WordDocument`, каждый из которых
# переопределяет метод `print_info()`.
# Задача:
# Напиши функцию `print_document_info(doc)`, которая принимает объект и вызывает
# его метод `print_info()`.
# Создай список из разных документов и передай их в эту функцию по очереди.

class Document: 
    def print_info(self):
        print('Это базовый документ')

class PDFDocument(Document):
    def print_info(self):
        print('Это PDF-документ')

class WordDocument(Document):
    def print_info(self):
        print('Это Word-документ')
    
class_list = [Document(), PDFDocument(), WordDocument()]

def print_document_info(doc):
    doc.print_info()

for doc in class_list:
    print_document_info(doc)


# Таск 2. Животные говорят
# Описание:
# Базовый класс `Animal` с методом `make_sound()`.
# Подклассы: `Dog`, `Cat`, `Cow`, каждый переопределяет `make_sound()` своим способом.
# Задача:
# Напиши функцию `make_animals_talk(animals: list)`, которая вызывает `make_sound()`
# для каждого животного.

class Animal:
    def make_sound(self):
        ...
class Dog(Animal):
    def make_sound(self):
        print('гав-гав')

class Cat(Animal):
    def make_sound(self):
        print('мяу-мяу')

class Cow(Animal):
    def make_sound(self):
        print('муу-муу')

animal = [Dog(), Cat(), Cow()]

def make_animals_talk(animal: list):
    for sound in animal:
        sound.make_sound()

make_animals_talk(animal)



# Таск 3. Игрушки
# Описание:
# Базовый класс `Toy` с методом `play_sound()`.
# Подклассы: `Car`, `Doll`, `Drum`.
# Задача:
# Симулируй работу магазина: перебери список из разных игрушек и запусти их звук.

class Toy:
    def play_sound(self):
        print('Звуки игрушек')

class Car(Toy):
    def play_sound(self):
        print('Дырдырдырдыр')

class Doll(Toy):
    def play_sound(self):
        print('Я люблю тебя')

class Drum(Toy):
    def play_sound(self):
        print('БАМ-БАМ')

toys_list = [Toy(), Car(), Doll(), Drum()]

def market(toys: list):
    for toy in toys:
        toy.play_sound()

market(toys_list)



# Таск 4. Фигуры и площадь
# Описание:
# Базовый класс `Shape` с методом `area()`.
# Подклассы: `Circle`, `Rectangle`, `Triangle`.
# Задача:
# Создай список из разных фигур и выведи их площади через один цикл. Используй
# `math.pi`, если надо.

import math
class Shape:
    def area(self):
        print('Площади фигур')

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(f'Площадь круга: {math.pi * self.radius**2}')

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        print(f'Площадь прямоугольника: {self.width * self.height}')

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        print(f'Площадь треугольника: {0.5 * self.base * self.height}')

shapes_list = [Shape(), Circle(5), Rectangle(3, 4), Triangle(6, 2)]

for shape in shapes_list:
    shape.area()

# Таск 5. Банкомат
# Описание:
# Базовый класс `Card`, метод `withdraw(amount)`.
# Подклассы: `CreditCard` (может уходить в минус), `DebitCard` (не может уходить в
# минус).
# Задача:
# Симулируй списание денег с разных карт, используя одну и ту же функцию.

class Card:
    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount

    def set_balance(self, amount):
        self.__balance = amount

    def withdraw(self):
        ...

class CreditCard(Card):
    def withdraw(self, amount):
        new_balance = self.balance - amount
        self.set_balance(new_balance)

class DebitCard(Card):
    def withdraw(self, amount):
        if self.balance >= amount:
            new_balance = self.balance - amount
            self.set_balance(new_balance)
        else:
            print(f'Не хватает средств, возможно снять {self.balance}')

obj_Credit = CreditCard()
obj_Card = Card()
obj_Credit.deposit(4500)
obj_Credit.withdraw(5000)
obj_Credit.withdraw(6000)
print(obj_Credit.balance)

obj_Debit = DebitCard()
obj_Debit.deposit(5000)
obj_Debit.withdraw(6000)


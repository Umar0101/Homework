# class Transport:
#     def move(self):
#         ...

# class car(Transport):
#     def move(self):
#         print('брбрбр')
    
# class Bike(Transport):
#     def move(self):
#         print('дррррррррррррр')


# 2. Создайте класс `Employee` с атрибутами `name` и `salary`. Создайте класс `Manager`, унаследованный от `Employee`, добавьте атрибут `department` и метод `show_info()`.

# class Employee:
#     name = 'Umar'
#     salary = '1000000$'

# class Manager(Employee):
#     departament = 'UMAR'
#     def show_info(self):
#         print(super().name, super().salary, self.departament)

# 2. Создайте класс `Student` с приватными полями `name` и `grade`. Реализуйте методы доступа (геттеры и сеттеры) с проверкой допустимости оценки (0–100).

# class Student:
#     def __init__(self, name, grade):
#         self.__name = name
#         self.__grade = grade

#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self, name):
#         self.__name = name 


#     @property
#     def grade(self):
#         return self.__grade

#     @grade.setter
#     def grate(self, grade):
#         if grade < 1 or grade > 100:
#             print('Нельзя ставить оценку меньше 1 и больше 100')
 
#         else:
#             self.__grade = grade

# obj = Student('Umar', 100)

# obj.grade = 1000

# print(f'{obj.name} {obj.grade}')


# 2. Создайте базовый класс `Shape` с методом `area()`. Создайте классы `Rectangle` и `Circle`, реализующие метод `area()` по-своему. Используйте цикл для вычисления площадей разных фигур.

class Shape:
    def area():
        ...

class Rectangle:
    def area():
        ...

class Circle:
    def area():
        ...


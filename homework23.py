'================================ Umar ===================================='
# ИНКАПСУЛЯЦИЯ:
#     1) Создай класс BankAccount с приватным __balance. Добавь методы:
# 	    1) deposit(amount) – пополнение баланса
# 		2) withdraw(amount) – снятие (он должен снимать не больше текущего баланса)
# 		3) get_balance() – возвращает баланс

class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
obj1 = BankAccount()

obj1.deposit(200000)
obj1.withdraw(30000)
print(obj1.get_balance())
        

#     2) Создай класс User в котором (задание по теме getters/setters):
# 		1) name — публичный атрибут
# 		2) password — приватный атрибут
# 		3) Метод get_password() который будет возвращать * вместо пароля
# 		4) Метод set_password(new_password), который будет проверять длину пароля, 
#         и если она больше 6 символов, то меняет предыдущий на новый
#         ПРИМЕЧАНИЕ: пароль должен состоять из букв и цифр

class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password 

    def get_password(self):
        return '*' * len(self.__password)
        
    def set_password(self, new_password):
        if len(new_password) > 6 and new_password.isalnum():
            self.__password = new_password
            print('У вас новый пароль')
        else:
            print('Вы ввели некорректный пароль')

obj2 = User('Umar', '3456789')

obj2.set_password('ojojooj5')
print(obj2.get_password())


#     3) Создайте класс Employee у которого есть:
# 		1) name – имя сотрудника
# 		2) __salary (приватный атрибут)
# 		3) salary (геттер) – возвращает зарплату
# 		5) salary (сеттер) – изменяет зарплату (не меньше 30_000)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary > 30000:
            self.__salary = new_salary
        else:
            print('Зарплата должна состоять не меньше 30.000')
        
obj3 = Employee('Umar', 30001)

obj3.salary = 40000
print(obj3.salary)

#     4) Создайте класс Circle у которого есть:
# 		1) radius (геттер/сеттер, не < 0).
# 		2) area (геттер) – вычисляет площадь (число пи * радиус в квадрате).

#         Затем:

#         Создайте дочерний класс Cylinder(Circle) и добавьте в него:
# 		    1)height (геттер/сеттер, не < 0)

import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
        
    @radius.setter
    def radius(self, new_radius):
        if new_radius >= 0:
            self.__radius = new_radius
        else:
            print('радиус не может быть меньше 0')

    @property
    def area(self):
        return math.pi * self.radius ** 2


class Cylinder(Circle):
    def __init__(self, height, radius):
        super().__init__(radius)
        self.__height = height

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, new_height):
        if new_height >= 0:
            self.__height = new_height
        else:
            print('Высота не может быть меньше 0')
        
    @property
    def volume(self):
        return math.pi * self.radius**2 * self.height
    
obj4 = Circle(20)

print(obj4.area)
print(obj4.radius)

obj_Cylin = Cylinder(20, 20)
print(obj_Cylin.height)
print(obj_Cylin.volume)



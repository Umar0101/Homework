'=========== Umar ============'

# Задание: Определите ошибки и исправьте код

# В каждом из приведенных ниже примеров есть ошибка.

# 1. Запустите код в интерпретаторе Python.
# 2. Запишите, какая ошибка будет выведена.
# 3. Объясните, что означает эта ошибка и как её можно исправить.

# Пример 1:
'''
x = "10" + 5
Исключение:
    TypeError: can only concatenate str (not "int") to str
Объяснение:
    Выходит потому что питон не может сделать конкатенацию между строкой и числом  
Исправленный вариант:
    x = '10' + '5'
'''

# Пример 2:
'''
numbers = [1, 2, 3]
print(numbers[5])
Исключение:
    IndexError: list index out of range
Объяснение:
    Выходит потому что в списке несуществует элемент по этому индексу   
Исправленный вариант:
    numbers = [1, 2, 3]
    print(numbers[2])
'''
# Пример 3:
'''
age = "25"
print(age / 5)
Исключение:
    TypeError: unsupported operand type(s) for /: 'str' and 'int'
Объяснение:
    Выходит потому что мы не сможем сделать операцию деление между строкой и числом
Исправленный вариант:
    age = 25
    print(age / 5)
'''

# Пример 4:
'''
my_dict = {"name": "Alice", "age": 30}
print(my_dict["gender"])
Исключение:
    KeyError: 'gender'
Объяснение:
    Выходит потому что мы ссылаемся на несуществующему ключу
Исправленный вариант:
    my_dict = {"name": "Alice", "age": 30}
    print(my_dict["name"])
'''

# Пример 5:
'''
for i in range("5"):
print(i)
Исключение:
    IndentationError: expected an indented block after 'for' statement on line 60
Объяснение:
    Выходит потому что функция 'range' используется для генерации последовательностей чисел, а мы пытаемся использовать со строкой
Исправленный вариант:
    for i in range(1,6):
    print(i)
'''

# Пример 6:
'''
value = None
print(value + 10)
Исключение:
    TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
Объяснение:
    Выходит потому что оператор '+' не поддерживает для 'NoneType' and 'int'
Исправленный вариант:
    value = 10
    print(value + 10)
'''

# Пример 7:
'''
a = 10
b = 0
result = a / b
print(result)
Исключение:
    ZeroDivisionError: division by zero
Объяснение:
    Выходит при делении на 0
Исправленный вариант:
    a = 10
    b = 1
    result = a / b
    print(result)
'''

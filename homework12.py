'===========  Umar  ============='

# Задание 1: Создание словарей

# 1. Создайте словарь, в котором хранятся следующие данные о студенте:
# • Имя: “Аружан”
# • Возраст: 20
# • Группа: “IS-23”
# 2. Выведите имя студента, используя ключ.
# 3. Обновите группу студента на “CS-25”.
# 4. Добавьте новый ключ hobby со значением “чтение”.
# 5. Выведите обновленный словарь.

dict1 = {
    'name': 'Аружан',
    'age': 20,
    'group': 'IS-23'
}

print(dict1['name'])
dict1['group'] = 'CS-25'
dict1['hobby'] = 'чтение'
print(dict1)

'------------------------------------------------------------'

# Задание 2: Работа с методами словаря

# Дан словарь:

# grades = {'math': 90, 'history': 85, 'english': 88}

# 1. Получите значение по ключу math, используя метод get.
# 2. Попробуйте получить значение по ключу science с дефолтным значением "Не найдено".
# 3. Удалите предмет history и выведите его значение.
# 4. Удалите последний предмет из словаря, используя метод popitem, и выведите его.
# 5. Добавьте новый предмет 'physics': 92 в словарь, используя метод update.

grades = {'math': 90, 'history': 85, 'english': 88}
print(grades.get('math'))
print(grades.get('science', 'не найдено'))
print(grades.pop('history'))
print(grades.popitem())
grades.update({'physics':92})
print(grades)

'---------------------------------------------------------------'

# Задание 3: Работа с методом fromkeys

# 1. Создайте список ключей:

# keys = ['name', 'age', 'city']


# 2. Используя метод fromkeys, создайте словарь, где значением для всех ключей будет строка "unknown".
# 3. Обновите значения:
# • Для ключа 'name' установите "Али".
# • Для ключа 'age' установите 25.
# • Для ключа 'city' установите "Алматы".
# 4. Выведите итоговый словарь.

keys = ['name', 'age', 'city']
dict1 = dict.fromkeys(keys, "unknown")
dict1['name'] = 'Али'
dict1['age'] = 25
dict1['city'] = 'Алматы'
print(dict1)

'----------------------------------------------------------------'

# Задание 4: Создание словаря из списка

# Дан список имен:

# names = ['Али', 'Айдана', 'Ермек']

# 1. Создайте словарь, где ключами будут имена, а значениями — их длина.
# Пример:

# {'Али': 3, 'Айдана': 6, 'Ермек': 5}

names = ['Али', 'Айдана', 'Ермек']

dict1 = {}
for i in names:
    dict1[i] = len(i)
print(dict1)

# 2. Используйте метод fromkeys, чтобы создать словарь, где все имена будут ключами, а значением будет строка "unknown".

dict2 = dict.fromkeys(dict1,'unknown')
print(dict2)

# 3. Обновите значение для имени 'Али' на "student".

dict2['Али'] = 'student'

'---------------------------------------------------------------------'

# Задание 5: Итерация по словарю

# Дан словарь:

user_info = {
'name': 'Диана',
'age': 22,
'city': 'Алматы',
'profession': 'дизайнер'
}

# 1. Напишите цикл, который выводит только ключи.
# 2. Напишите цикл, который выводит только значения.
# 3. Напишите цикл, который выводит пары ключ:значение в формате:

# Ключ: name, Значение: Диана

for i in user_info.keys():
    print(i)                # выводит только ключи.

for i in user_info.values():
    print(i)             # выводит только значения.

for key, value in user_info.items():
    print(f'Ключ: {key}, Значение: {value}')  # выводит пары ключ:значение в формате: Ключ: name, Значение: Диана

'---------------------------------------------------------------------------'

# Задание 6: Задача на логику

# Вам дан словарь:

# products = {'apple': 50, 'banana': 30, 'cherry': 60}

# 1. Напишите код, который увеличивает цену каждого продукта на 10%.
# Пример:

# {'apple': 55, 'banana': 33, 'cherry': 66}

products = {'apple': 50, 'banana': 30, 'cherry': 60} 
products1 ={}
for i,b in products.items():
    products1[i]= int(b*1.1)
print(products1)

# 2. Удалите продукт с наименьшей ценой из словаря.
# products2 = {}

min_elem = min(products1.values())

for k, v in products1.items():
    if v == min_elem:
        products1.pop(k)
        break
    
# 3. Добавьте новый продукт 'orange': 40.

products1['orange'] = 40 

# 4. Напишите цикл, который выводит все продукты с ценой выше 50.

for i, b in products1.items():
    if b > 50:
        print(f'{i}: {b}')

'===============  Umar  ============'

# Создай программу для обработки списка покупок и строки с текстом. Программа должна:

# 1. Запросить у пользователя строку товаров, разделённых запятыми (например, “молоко, хлеб, яблоки, сыр”).
# • Используй split, чтобы превратить строку в список.

# 2. Попросить пользователя ввести дополнительные товары через пробел. Эти товары нужно добавить к списку.
# • Используй extend, чтобы расширить список.

# 3. Вывести текущий список товаров, а затем предложить пользователю:
# • Удалить последний товар (используй pop или reverse + pop).
# • Развернуть список (используй reverse).
# • Отсортировать его (используй sort).

# 4. Проверить длину списка и вывести её (используй len).

# 5. Предложить очистить список:
# • Если пользователь согласится, используй clear.
# • Если нет, выведи сообщение с текущими товарами.

# 6. Цикл for: Пройтись по списку и вывести все товары с порядковым номером.

# 7. Множественное присваивание: Выбрать два любых товара из списка (например, первый и последний) и через множественное присваивание поменять их местами. (посмотрите самостоятельно, как менять значение в списке по индексу)

# 8. Функция join: Объединить список в строку, где товары разделены символом “;”, и вывести её.


# Пример выполнения программы:

# Ввод: (то, что будет выводиться в консоли)

# Введите список товаров через запятую: (например введем: молоко, хлеб, сыр)
# Введите дополнительные товары через пробел: (например введем: яйца бананы)

# Вывод:

# Ваш список: ['молоко', 'хлеб', 'сыр', 'яйца', 'бананы']
# Хотите развернуть список? (да/нет): (например: да)
# Ваш список: ['бананы', 'яйца', 'сыр', 'хлеб', 'молоко']
# Хотите отсортировать список? (да/нет): (например: да)
# Ваш список: ['бананы', 'хлеб', 'молоко', 'сыр', 'яйца']
# Длина списка: 5
# Хотите очистить список? (да/нет): (например: нет)
# Ваш список: ['бананы', 'хлеб', 'молоко', 'сыр', 'яйца']
# Ваши товары по порядку:
# 1. бананы
# 2. хлеб
# 3. молоко
# 4. сыр
# 5. яйца
# Меняем местами первый и последний товары.
# Обновлённый список: ['яйца', 'хлеб', 'молоко', 'сыр', 'бананы']
# Объединённый список: яйца; хлеб; молоко; сыр; бананы

tovar = input('Введите товары через запятые: ')
tovar_list = tovar.split(', ')
tovar2 = input('Введите дополнительные товары через пробелы: ')
tovar2_list = tovar2.split()
tovar_list.extend(tovar2_list)
print('Ваш список:',tovar_list)

if input('хотите развернуть список? да или нет: ') == 'да': 
    tovar_list.reverse()
    print('Ваш список:',tovar_list)
else:
    print('Ваш список:',tovar_list)

if input('Хотите отсортировать список? да или нет: ') == 'да':
    tovar_list.sort()
    print('Ваш список:',tovar_list)
else:
    print('Ваш список:',tovar_list)

print('длина списка:',len(tovar_list))    

if input('Хотите очистить список? да или нет: ') == 'да':
    tovar_list.clear()
    print('Ваш список:',tovar_list)
    exit()
else:
    print('Ваш список:',tovar_list)

s = 0
for i in tovar_list:
    s += 1
    print(s,i)

tovar_list[0], tovar_list[-1] = tovar_list[-1], tovar_list[0]

print('Обновленный список:', tovar_list)
str1 = '; '.join(tovar_list)
print('Объединенный список:', str1)

# Вот доп задание для практики:

# 1 Задание: Напишите программу, которая:

# 1. Запрашивает у пользователя строку.
# 2. Использует цикл for для подсчёта количества гласных букв (а, е, ё, и, о, у, ы, э, ю, я) в строке.
# 3. Выводит количество гласных.
# (Подсказка:
# Используйте условие if внутри цикла для проверки, является ли символ гласной.)

quest = input('Введите строку: ')
gls = 0
vse_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
for i in quest:
    if i in vse_gls:
                gls += 1

print('Кол-во гласных:', gls)
    

# 2 Задание: Напишите программу, которая:

# 1. Запрашивает у пользователя список чисел через пробел.
# 2. Использует цикл for для создания нового списка, состоящего только из чётных чисел.
# 3. Выводит новый список.

spisok = (input('Введите список через пробел: '))
list1 = list(map(int, spisok.split()))
list2 = []
for i in list1:
        if i%2==0:
            list2.append(i)

print('список четных чисел:',list2)
                
# 3 Задание: Напишите программу, которая:

# 1. Задаёт заранее известное слово (например, python).
# 2. Запрашивает у пользователя строку.
# 3. Использует цикл for для проверки, какие буквы из слова пользователь угадал, и выводит их.
# 4. Если буквы нет, вместо неё выводится _.

python_ = 'python'
str1 = input('введите строку: ').lower()
str2 = ''
for i in python_:
        if i in str1:
            str2 += i
        else:
            str2 += '_'
print(str2)

# Пример:
# Слово: python
# Ввод: phx
# Вывод: p_h___

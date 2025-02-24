'============================ Umar =============================='
# BUILT-INS:
#     1) Даны два списка:
#     names = ['Nikita', 'Katana', 'Toma']
#     ages = [25, 30, 35]
#     Создайте словарь, в котором ключи — это имена, а значения — соответствующие им возраста

names = ['Nikita', 'Katana', 'Toma']
ages = [25, 30, 35]
key_name = dict(zip(names, ages))
print(key_name)


#     2) Дана строка:
#     text = "python"
#     при помощи определенной встроенной функции выведите индексы и символы, начиная с 1

text = "python"
enum = enumerate(text, 1)
for x,y in enum:
    print(x,y)


#     3) Дан список строк с числами:
#     numbers = ["10", "20", "30", "40"]
#     Преобразуйте его в список целых чисел

numbers = ["10", "20", "30", "40"]
str_numbers = list(map(int, numbers))
print(str_numbers)


#     4) Дан список слов:
#     words = ["apple", "banana", "cherry", "dog", "elephant"]
#     Отфильтруйте и оставьте только те слова, которые начинаются с буквы d

words = ["apple", "banana", "cherry", "dog", "elephant"]
filter_words = list(filter(lambda x: x.startswith('d'), words))
print(filter_words)


#     5) Дан список чисел:
#     numbers = [1, -2, 3, -4, 5, -6]
#     Сначала удалите отрицательные числа при помощи filter, затем возведите оставшиеся числа в квадрат с помощью map

numbers = [1, -2, 3, -4, 5, -6]
filter_numbers = filter(lambda x: x>0, numbers)
filter_numbers = list(map(lambda x: x**2, filter_numbers))
print(list(filter_numbers))


#     6) Даны два списка:
#     students = ["Alice", "Bob", "Charlie", "David"]
#     scores = [85, 92, 78, 90]
#     УСЛОВИЯ ЗАДАНИЯ:
#     	1.	Используйте zip, чтобы соединить студентов и их оценки
# 	    2.	С помощью filter оставьте только тех, у кого оценка больше 80
# 	    3.	Пронумеруйте оставшихся студентов, начиная с 1, используя enumerate
# 	    4.	Преобразуйте результат в список кортежей (номер, имя, оценка)
        
students = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 90]

students_scores = list(zip(students, scores))
students_scores = list(filter(lambda x: x[1] > 80, students_scores))
students_scores = enumerate(students_scores, 1)
print(list(students_scores))
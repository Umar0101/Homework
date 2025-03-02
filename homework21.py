'==== Umar ===='

# ДЕКОРАТОРЫ:
    # 1) Напишите декоратор, который перед вызовом функции будет выводить сообщение "Выполнение функции..."

def func_start(func):
    def wrapper (*args, **kwargs):
        print('Выполнение функции сложения')
        func()
    return wrapper
    
def sum():
    x = int(input('1 число: '))
    y = int(input('2 число: '))
    print(f'{x} + {y} = {x+y}')

func_start(sum)()


    # 2) Создайте декоратор, который будет умножать результат выполнения числовой функции на 2

def func_mult(func):
    def wrapper(*args,**kwargs):
        print('результат функции')
        res = func(*args,**kwargs)
        print(res)
        print('умножение резултата функции на 2')
        print(res * 2)
    return wrapper

@func_mult    
def func_num(x, y):
    return x + y

func_num(4, 4)


    # 3) Создайте декоратор, который к строковому результату функции добавляет "!" в конце

def str_(func):
    def wrapper(*args, **kwargs):
        res = func(*args,**kwargs)
        res = res + '!'
        return res
    return wrapper

@str_
def exclamation(x):
    return x
        
print(exclamation('с днем рождения'))


    # 4) Создайте декоратор, который ограничит выполнение функции 3 вызовами
    # Если функция вызывается больше 3 раз, выводить сообщение "Функция больше недоступна"

def counter_decorator(func):
    def wrapper(*args, **kwargs):
        if wrapper.count < 3:
            wrapper.count += 1
            return func(*args, **kwargs)
        else:
            return "Функция больше недоступна"
    wrapper.count = 0
    return wrapper

@counter_decorator
def my_func(x):
    return x

for i in range(4):
    print(my_func("Hi"))


    # 5) Создайте декоратор, который будет выводить переданные аргументы перед вызовом функции

def func_decorator(func):
    def wrapper(*args, **kwargs):
        print(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@func_decorator
def my_func(x):
    return x ** 2
print(my_func(5))
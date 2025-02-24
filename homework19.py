'==================== Umar ========================='

# КАЛЬКУЛЯТОР ИСПОЛЬЗУЯ СЛОВАРЬ И LAMBDA ФУНКЦИИ:
#     Напишите Калькулятор, который:
# 	1) Запрашивает у пользователя два числа.
# 	2) Запрашивает у пользователя операцию (+, -, *, /).
# 	3) Использует lambda-функции для выполнения соответствующей операции.
# 	4) Выводит результат на экран.
# 	5) Программа должна корректно обрабатывать деление на ноль(используйте try except)
# 	6) Можно использовать if-else для выбора нужной lambda-функции.
# 	7) реализовать программу с помощью словаря, где ключи — операции (+, -, *, /), а значения — соответствующие lambda-функции.

# **ПРИМЕЧАНИЕ: СРОК ВЫПОЛНЕНИЯ БУДЕТ СТОЯТЬ НА ПОНЕДЕЛЬНИК СЛЕДУЮЩЕЙ НЕДЕЛИ, ЗАДАЧА НЕОБЫЧНАЯ И НЕМНОГО ТРУДНАЯ, ПОЭТОМУ БУДЕТ ДАНО БОЛЬШЕ ВРЕМЕНИ**


lambda_calculator = [{'+': lambda x, y: x + y,
                      '-': lambda x, y: x - y,
                      '*': lambda x, y: x * y,
                      '/': lambda x, y: x / y,
                      '//': lambda x, y: x // y,
                      '**': lambda x, y: x ** y,
                      '%': lambda x, y: x % y}]
 

for oper in lambda_calculator:
    try:
        num1 = int(input('Введите первое число: '))
        operator = input('Введите операцию: ')
        num2 = int(input('Введите второе число: '))
    except ValueError:
        print('Вы ввели букву!')
        break
    if operator == '+':
        print(oper['+'](num1,num2))
    elif operator == '-':
        print(oper['-'](num1,num2))
    elif operator == '*':
        print(oper['*'](num1,num2))
    elif operator == '/':
        try:
            print(oper['/'](num1,num2))
        except ZeroDivisionError:
            print('На ноль делить нельзя!')
    elif operator == '//':
        print(oper['//'](num1,num2))
    elif operator == '**':
        print(oper['**'](num1,num2))
    elif operator == '%':
        try:
            print(oper['%'](num1,num2))
        except ZeroDivisionError:
            print('На ноль нельзя!')
    else:
        print('Такая операция не существует!')

# Создать калькулятор.

#greeting = int(input(f'Калькулятор приветствует тебя!)'))

number_1 = int(input('Введите первое значение: '))

operation = input(f'Выберите действие: +, -, *, /   ')
#+ for addition
#- for subtraction
#* for multiplication
#/ for division

number_2 = int(input('Введите второе значение: '))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)
elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)
elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)
elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)
else:
    print('Вы ввели неверный оператор действия. Повторите попытку.')


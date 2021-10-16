"""
Функция factorial(number):
Если number = 1:
    Вернуть 1
Иначе:
    Вернуть number * factorial(number - 1)

Функция sum_number_factorial(number):
Создаем переменную number и присваиваем результат функции factorial(number)
С помощью генератора списков создать список с цифрами числа number
Просумировать с помощью функции sum()
"""


def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def sum_numbers_factorial(number):
    number = factorial(number)
    lst = [int(i) for i in str(number)]
    return sum(lst)


print(sum_numbers_factorial(100))

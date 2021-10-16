"""
С помощью функции pow() найти число 2^1000 засунуть его в переменную number
Циклом перебрать все цифры имеющегося числа-строки
Вывести число
"""


def degree_sum(number, sum=0):
    number = pow(number, 1000)
    for i in str(number):
        sum += int(i)
    return sum


print(degree_sum(2))

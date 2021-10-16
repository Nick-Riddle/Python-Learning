"""
Создать пустой список для хранения слагаемых
Создать переменную temp (для хранения последующего шага)
Цикл while пока сумма списка не равна даному числу:
    Если сумма больше данного числа:
        обнуляем список
        temp += 1
        counter = temp
    добавляем к списку counter
"""

number = int(input())


def sum_of_number(number):
    if number == 1 or number == 2:
        return [number]
    lst = []
    for n in range(1, number + 1):
        number -= n
        if number > n:
            lst.append(n)
        else:
            lst.append(number)
    return lst


rez = sum_of_number(number)
print(len(rez))
for i in rez:
    print(i, end=' ')




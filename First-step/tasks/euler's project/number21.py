"""
Создать пустой словарь (для сохранения числа: сумы его делителей)
Создать функцию для расчета сумы делителей всех чисел до 10000 и записи их в словарь:
    Цикл от 1 до number:
        Если number == 1:
            Вернуть один
        Если число делится на элемент цикла нацело:
            sum += элемент цикла
    Записать в словарь ключ-значение
    Вернуть эту же функцию но уже с number - 1
Создать функцию для расчета суммы всех дружественных чисел:
    Если в словаре есть одинаковые сумы делителей, то просуммировать числа с которых они сделаны
    Вернуть сумму
"""
dictionary = {}


def sum_divisors(number, dict):
    sum = 0
    for i in range(1, number):
        for j in range(1, i):
            if i % j == 0:
                sum += j
        if sum != i:
            dict[i] = sum
        sum = 0
    pass


def bag_friendly_numbers(dict):
    lst = []
    for i in range(9999, 0, -1):
        if i in dict and dictionary[i] in dict and dictionary[dictionary[i]] == i:
            lst.append(i)
    return sum(lst)


sum_divisors(10000, dictionary)
print(bag_friendly_numbers(dictionary))

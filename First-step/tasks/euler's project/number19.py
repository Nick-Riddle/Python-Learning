"""
Создать словарь с месяцами (номер месяца: количество дней)
Создать переменную sundays (количество недель)
Создать переменную days (будем ей присваивать количество дней определенного месяца)
Цикл перебора годов (1900 - 2001):
    Цикл перебора месяцев (1, 13):
        Присваиваем days количество дней текущего месяца
        Цикл пока days - 6 не будет меньше-равно 0:
        Если разница между days последующего месяца и days текущего равна единице:
            sundays += 1
"""

months = {1: 31,
          2: 28,
          3: 31,
          4: 30,
          5: 31,
          6: 30,
          7: 31,
          8: 31,
          9: 30,
          10: 31,
          11: 30,
          12: 31}


def number_sundays(months):
    sundays = 0
    days = 7
    for i in range(1900, 2001):
        if (i % 4 == 0 and str(i)[2:] != "00") or (str(i)[2:] == "00" and i % 400 == 0):
            months[2] = 29
        else:
            months[2] = 28
        for j in range(1, len(months) + 1):
            while days <= months[j]:
                days += 7
            if days - months[j] == 1:
                sundays += 1
            days -= months[j]
        if i == 1900:
            sundays = 0
    return sundays


print(number_sundays(months))

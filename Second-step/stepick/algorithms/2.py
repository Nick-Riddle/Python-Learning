"""
Список с отрезками и их 'координатами'
Функция для сортировки отрезков по правому краю:
    Создаем отсортированный список
    Цикл по списку:
        Берем наименьшую правую координату и добавляем в новый список
        Цикл пока все последующие координаты меньше текущей:
            Выкинуть со списка


Функция вывода результата:
    Выводим длину отсортированного списка
    Выводим через пробел координаты правого конца каждого с отрезков
"""

lst = [(4, 7), (1, 3), (2, 5), (5, 6)]


def sort_lst(l):
    temp_lst = []
    new_lst = []
    for item in l:
        temp_lst.append(item[1])
    temp_lst.sort()
    for i in temp_lst:
        for item in l:
            if i == item[1] and item not in new_lst:
                new_lst.append(item)
    print(new_lst)
    for i in range(len(new_lst)):
        if i >= len(new_lst):
            i -= 1
        if new_lst[i] != new_lst[0] and new_lst[i][0] <= new_lst[new_lst.index(new_lst[i - 1])][1]:
            new_lst.remove(new_lst[i])
    return new_lst


def output_lst(l):
    print(len(l))
    for item in l:
        if item != l[-1]:
            print(item[1], end=', ')
        else:
            print(item[1])


output_lst(sort_lst(lst))

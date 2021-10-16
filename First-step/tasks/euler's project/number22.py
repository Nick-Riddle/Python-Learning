"""
Создать переменную points (очки имени) и sum_points (сумма всех очков имен)
Цикл для каждого из имен в списке:
    Цикл для каждой букве из имен:
        Добавить к points очки в dictionary
    Умножить points на индекс имени в списке
    Добавить к sum_points points
    Обнулить points
"""

names = []
dictionary = {'A': 1,
              'B': 2,
              'C': 3,
              'D': 4,
              'E': 5,
              'F': 6,
              'G': 7,
              'H': 8,
              'I': 9,
              'J': 10,
              'K': 11,
              'L': 12,
              'M': 13,
              'N': 14,
              'O': 15,
              'P': 16,
              'Q': 17,
              'R': 18,
              'S': 19,
              'T': 20,
              'U': 21,
              'V': 22,
              'W': 23,
              'X': 24,
              'Y': 25,
              'Z': 26}


def reading_file(name):
    f = open('p022_names.txt', 'r')
    temp = ''
    counter = 0
    for line in f:
        for underline in line:
            if underline == ',':
                name.append(temp.replace('"', ''))
                counter = 0
                temp = ''
            else:
                temp += underline
                counter += 1
        name.append(temp.replace('"', ''))
    f.close()
    pass


def points_for_names(name, dict):
    name.sort()
    points = 0
    sum_points = 0
    for line in name:
        for underline in line:
            points += dictionary[underline]
        sum_points += points * (name.index(line) + 1)
        points = 0
    return sum_points


reading_file(names)
print(points_for_names(names, dictionary))


"""
Функция для чтения из файла, более разумная:
    def get_names():
        parts=[]
        f = open('c:\\exp\\names.txt')
        line = f.readline()
        tmp=line.split(',')
        for i in tmp:
            b=i.strip('"')
            parts.append(b)
        parts.sort()
        return parts
"""
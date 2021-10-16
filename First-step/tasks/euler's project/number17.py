"""
Создать словарь со всеми ключевыми словами (число: буквенный вид)
Создать два списка (первый для чисел, второй для буквенного вида)
Генератором списков сделать список от 1 до 1000 включительно
Для каждого элемента первого списка определить буквенный вид с помощью словаря и засунуть во второй список
Просуммировать количество букв каждого элемента второго списка
"""

dictionary = {1: "one",
              2: "two",
              3: "three",
              4: "four",
              5: "five",
              6: "six",
              7: "seven",
              8: "eight",
              9: "nine",
              10: "ten",
              11: "eleven",
              12: "twelve",
              13: "thirteen",
              14: "fourteen",
              15: "fifteen",
              16: "sixteen",
              17: "seventeen",
              18: "eighteen",
              19: "nineteen",
              20: "twenty",
              30: "thirty",
              40: "forty",
              50: "fifty",
              60: "sixty",
              70: "seventy",
              80: "eighty",
              90: "ninety",
              100: "hundred",
              1000: "thousand"}


def letter_count(dictionary):
    numbers = [i for i in range(1, 1001)]
    letters = []
    length = 0
    for i in numbers:
        if i <= 20:
            letters.append(dictionary[i])
        elif i < 100:
            if int(str(i)[1]) != 0:
                letters.append(dictionary[int(str(i)[0]) * 10] + "-" + dictionary[int(str(i)[1])])
            else:
                letters.append(dictionary[i])
        elif i == 1000:
            letters.append(dictionary[int(str(i)[0])] + " " + dictionary[1000])
        else:
            if int(str(i)[1]) == 0 and int(str(i)[2]) == 0:
                letters.append(dictionary[int(str(i)[0])] + " " + dictionary[100])
            elif int(str(i)[1]) == 0 and int(str(i)[2]) != 0:
                letters.append(dictionary[int(str(i)[0])] + " hundred and " + dictionary[int(str(i)[2])])
            elif int(str(i)[1]) != 0 and int(str(i)[2]) == 0:
                letters.append(dictionary[int(str(i)[0])] + " hundred and " + dictionary[int(str(i)[1]) * 10])
            elif int(str(i)[1:]) < 20:
                letters.append(dictionary[int(str(i)[0])] + " hundred and " + dictionary[int(str(i)[1:])])
            else:
                letters.append(dictionary[int(str(i)[0])] + " hundred and " + dictionary[int(str(i)[1]) * 10] + "-" + dictionary[int(str(i)[2])])
    for i in letters:
        length += len(i.replace(' ', '').replace('-', ''))
    return length


print(letter_count(dictionary))

"""
Создать словарь для хранения буквы: количество раз в строке
Прочитать символ каждой строки, запихнуть в словарь
Создать второй словарь для хранения буквы: кода
Прочитать строку и декодировать
"""

string = str(input())
count_dictionary = {c: string.count(c) for c in set(string)}
sorted_dict = {}
sorted_keys = sorted(count_dictionary, key=count_dictionary.get)
for w in sorted_keys:
    sorted_dict[w] = count_dictionary[w]
code_lst = []


def coding():
    sorted_lst = list(sorted_dict.items())
    counter = 0
    while True:
        for item in sorted_lst:
            if code_lst != [] and code_lst[counter - 1][1] == '0':
                code_lst.append((item[0], '1'))
            else:
                code_lst.append((item[0], '0'))
            counter += 1
            if counter % 2 == 0:
                sorted_lst.append((sorted_lst[0][0] + sorted_lst[1][0], sorted_lst[0][1] + sorted_lst[1][1]))
                sorted_lst.pop(0)
                sorted_lst.pop(0)
                sorted_lst = sorted(sorted_lst, key=lambda counts: counts[1])
                counter = 0
                break
        if len(sorted_lst) == 1:
            break
    return code_lst


def decoding():
    code = coding()
    code_str = ''
    sub_str = ''
    codes = {}
    for letter in string:
        for item in code:
            if letter in item[0]:
                sub_str += item[1]
        code_str += sub_str[::-1]
        codes[letter] = sub_str[::-1]
        sub_str = ''
    print(len(list(codes.keys())), len(code_str))
    list_keys = sorted(list(codes.keys()))
    for i in list_keys:
        print(i + ":", codes[i])
    return code_str


print(decoding())
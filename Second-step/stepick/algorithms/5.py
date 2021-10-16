"""
size, length = map(int, input().split())
code_lst = [tuple(map(str, input().split())) for i in range(size)]
code_dict = {item[1]: item[0] for item in code_lst}
for item in code_dict:
    if ":" in code_dict[item]:
        code_dict[item] = code_dict[item].replace(":", "")
code_str = str(input())


def decoding():
    temp_str = ''
    rez_str = ''
    counter = 0
    while True:
        for i in range(counter, length):
            temp_str += code_str[i]
            for key in code_dict.keys():
                if temp_str in key:
                    break
            else:
                counter += len(temp_str[:-1])
                rez_str += code_dict[temp_str[:-1]]
                temp_str = ''
                break
        else:
            rez_str += code_dict[temp_str]
            break
    return rez_str


decoding()
"""

size, length = map(int, input().split())
code_lst = [tuple(map(str, input().split())) for i in range(size)]
code_dict = {item[1]: item[0] for item in code_lst}
for item in code_dict:
    if ":" in code_dict[item]:
        code_dict[item] = code_dict[item].replace(":", "")
code_str = str(input())


def decoding():
    global code_str
    rez_str = ''
    while code_str != '':
        for i in code_dict.keys():
            if code_str.startswith(i):
                rez_str += code_dict[i]
                code_str = code_str[len(i):]
                break


decoding()
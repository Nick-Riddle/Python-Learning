"""

"""

count_operations = int(input())
operations = [list(map(str, input().split())) for i in range(count_operations)]
for item in operations:
    item[0] = item[0].lower()
    if len(item) == 2:
        item[1] = int(item[1])
lst = []
for item in operations:
    if item[0] == 'insert':
        lst.append(item[1])
        break


def insert(element):
    lst.append(element)
    siftup(len(lst))
    pass


def siftup(index):
    while index > 1 and lst[index//2 - 1] < lst[index - 1]:
        lst[index//2 - 1], lst[index - 1] = lst[index - 1], lst[index//2 - 1]
        index //= 2
    pass


def extractmax():
    print(lst[0])
    lst[0] = lst[len(lst) - 1]
    lst.pop(len(lst) - 1)
    siftdown(1)
    pass


def siftdown(index):
    while 2*index - 1 < len(lst):
        j = index - 1
        j = lst.index(max(lst[2*(j+1)], lst[2*(j+1) - 1]))
        if j == index:
            break
        else:
            lst[index - 1], lst[j] = lst[j], lst[index - 1]
            index = j + 1
    pass


for i in range(1, count_operations):
    if operations[i][0] == 'insert':
        insert(operations[i][1])
    else:
        extractmax()


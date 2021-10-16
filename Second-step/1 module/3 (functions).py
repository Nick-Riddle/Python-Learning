length = int(input())
temp = ['global']
lst = ['global']


def add():
    lst.append(arg)


def create():
    lst.append(namesp)
    temp.append(namesp)


def get():
    global namesp
    if temp.index(namesp) != len(temp) - 1:
        new_namesp = temp[temp.index(namesp) + 1]
        if arg in lst[lst.index(namesp): lst.index(new_namesp) + 1]:
            print(namesp)
            return
    elif arg in lst[lst.index(namesp):]:
        print(namesp)
        return
    else:
        while namesp != temp[0]:
            temp_index = lst.index(namesp)
            namesp = temp[temp.index(namesp) - 1]
            if arg in lst[lst.index(namesp): temp_index]:
                print(namesp)
                return


for i in range(length):
    cmd, namesp, arg = input().split()
    if cmd == 'add':
        add()
    elif cmd == 'create':
        create()
    else:
        get()
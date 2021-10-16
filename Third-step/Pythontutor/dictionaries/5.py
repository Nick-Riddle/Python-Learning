dictionary = {}
for i in range(int(input())):
    lst = input().split()
    dictionary[lst[0]] = tuple(lst[1:])
for i in range(int(input())):
    act, name = input().split()
    if act == 'read':
        act = 'R'
    elif act == 'write':
        act = 'W'
    else:
        act = 'X'
    if name in dictionary and act in dictionary[name]:
        print('OK')
    else:
        print('Access denied')


'''
ACTION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}
 
file_permissions = {}
for i in range(int(input())):
    file, *permissions = input().split()
    file_permissions[file] = set(permissions)
 
for i in range(int(input())):
    action, file = input().split()
    if ACTION_PERMISSION[action] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')
'''

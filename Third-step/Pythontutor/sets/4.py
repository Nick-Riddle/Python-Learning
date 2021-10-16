mass, lst = set(), list(map(int, input().split()))
for i in lst:
    if i not in mass:
        mass.add(i)
        print('NO')
    else:
        print('YES')


'''
numbers = [int(s) for s in input().split()]
occur_before = set()
for num in numbers:
    if num in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(num)
'''

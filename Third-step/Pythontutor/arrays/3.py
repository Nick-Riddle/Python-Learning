n, m = map(int, input().split())
array = [['.'] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
            array[i][j] = '*'
for i in array:
    print(' '.join(i))


'''
n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        if (i + j) % 2 == 0:
            a[i].append('.')
        else:
            a[i].append('*')
for row in a:
    print(' '.join(row))
'''
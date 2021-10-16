n = int(input())
array = []
for i in range(n):
    array.append([])
    for j in range(n):
        if j == n - i - 1:
            array[i].append(1)
        elif j > n - i - 1:
            array[i].append(2)
        else:
            array[i].append(0)
for i in array:
    print(' '.join(list(map(str, i))))


'''
n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][n - i - 1] = 1
for i in range(n):
    for j in range(n - i, n):
        a[i][j] = 2
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
'''
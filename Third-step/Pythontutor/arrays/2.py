n = int(input())
array = [['.'] * n for i in range(n)]
for i in range(n):
    if i == round(n/2):
        for j in range(n):
            array[i][j] = '*'
    array[i][i] = '*'
    array[i][n - i - 1] = '*'
    array[i][round(n/2)] = '*'
for i in array:
    print(' '.join(i))

'''
n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][i] = '*'
    a[n // 2][i] = '*'
    a[i][n // 2] = '*'
    a[i][n - i - 1] = '*'
for row in a:
    print(' '.join(row))
'''
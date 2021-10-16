def swap_columns(a, i, j):
    for k in range(n):
        a[k][i], a[k][j] = a[k][j], a[k][i]


n, m = map(int, input().split())
array = [list(map(int, input().split())) for i in range(n)]
column_1, column_2 = map(int, input().split())
swap_columns(array, column_1, column_2)
for i in array:
    print(' '.join(list(map(str, i))))




'''
def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]
 
n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]
swap_columns(a, i, j)
print('\n'.join([' '.join([str(i) for i in row]) for row in a]))
'''
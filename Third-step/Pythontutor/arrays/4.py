n = int(input())
array = []
for i in range(n):
    array.append([])
    array[i].append(i)
    for j in range(1, n):
        array[i].append(abs(j - i))
for i in array:
    print(' '.join(list(map(str, i))))


'''
n = int(input())
a = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in a:
    print(' '.join([str(i) for i in row]))
'''
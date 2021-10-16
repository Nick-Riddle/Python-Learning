n, k = map(int, input().split())
lst, str = [tuple(map(int, input().split())) for i in range(k)], ['I'] * n
for i in lst:
    for j in range(i[0] - 1, i[1]):
        str[j] = '.'
print(''.join(str))


'''
n, k = [int(s) for s in input().split()]
bahn = ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        bahn[j] = '.'
print(''.join(bahn))
'''

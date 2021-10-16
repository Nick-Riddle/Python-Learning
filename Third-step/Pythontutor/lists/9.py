lst = list(map(int, input().split()))
for i in range(1, len(lst), 2):
    lst[i - 1], lst[i] = lst[i], lst[i - 1]
for i in lst:
    print(i, end=' ')


'''
a = [int(i) for i in input().split()]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))
'''

lst = list(map(int, input().split()))
k, c = map(int, input().split())
lst.append(c)
for i in range(k, len(lst)):
    lst[len(lst) - 1], lst[i] = lst[i], lst[len(lst) - 1]
print(' '.join([str(i) for i in lst]))


'''
a = [int(s) for s in input().split()]
a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = C
print(' '.join([str(i) for i in a]))
'''

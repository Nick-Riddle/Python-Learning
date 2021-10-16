lst, k = list(map(int, input().split())), int(input())
for i in range(k + 1, len(lst)):
    lst[i], lst[i - 1] = lst[i - 1], lst[i]
lst.pop()
print(' '.join([str(i) for i in lst]))


'''
a = [int(s) for s in input().split()]
k = int(input())
for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
print(' '.join([str(i) for i in a]))
'''

lst = list(map(int, input().split()))
for i in range(len(lst)):
    if i % 2 == 0:
        print(lst[i], end=' ')


'''
a = input().split()
for i in range(0, len(a), 2):
    print(a[i])
'''

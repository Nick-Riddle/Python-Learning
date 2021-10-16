lst, counter = list(map(int, input().split())), 0
for i in range(1, len(lst)):
    if lst[counter] < lst[i]:
        print(lst[i], end=' ')
    counter += 1


'''
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])
'''

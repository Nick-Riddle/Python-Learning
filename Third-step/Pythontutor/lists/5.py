lst, counter = list(map(int, input().split())), 0
for i in range(1, len(lst) - 1):
    if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
        counter += 1
print(counter)


'''
a = [int(i) for i in input().split()]
counter = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        counter += 1
print(counter)
'''

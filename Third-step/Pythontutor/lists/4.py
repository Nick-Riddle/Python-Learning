lst = list(map(int, input().split()))
for i in range(1, len(lst)):
    if (lst[i] >= 0 and lst[i - 1] >= 0) or (lst[i] < 0 and lst[i - 1] < 0):
        print(lst[i - 1], lst[i])
        break


'''
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break
'''

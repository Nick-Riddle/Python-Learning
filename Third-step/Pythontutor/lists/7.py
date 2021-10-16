lst, size, position = list(map(int, input().split())), int(input()), 1
for i in range(len(lst)):
    if lst[i] < size:
        break
    position += 1
print(position)


'''
a = [int(i) for i in input().split()]
x = int(input())
pos = 0
while pos < len(a) and a[pos] >= x:
    pos += 1
print(pos + 1)
'''

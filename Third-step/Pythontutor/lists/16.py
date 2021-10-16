lst = [list(map(int, input().split())) for i in range(8)]
str = 'NO'
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i][0] == lst[j][0] or lst[i][1] == lst[j][1] or abs(lst[i][0] - lst[j][0]) == abs(lst[i][1] - lst[j][1]):
            str = 'YES'
            break
print(str)


'''
n = 8
x = []
y = []
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)
 
correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False
 
if correct:
    print('NO')
else:
    print('YES')
'''

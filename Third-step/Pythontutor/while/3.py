n, a, b, c, counter = int(input()), 0, 1, 0, 1
while counter <= n:
    c, a = a + b, b
    b = c
    counter += 1
print(c)


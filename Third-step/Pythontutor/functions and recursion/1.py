def power(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return (1 / a) * power(a, n + 1)
    else:
        return a * power(a, n - 1)


print(power(float(input()), int(input())))


'''
def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res
 
print(power(float(input()), int(input())))
'''

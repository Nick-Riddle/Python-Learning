def power(a, n):
    if n == 1:
        return a
    else:
        return a * power(a, n - 1)


print(power(float(input()), int(input())))

'''
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
 
print(power(float(input()), int(input())))
'''
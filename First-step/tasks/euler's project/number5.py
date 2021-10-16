def least_multiple():
    n = 2520
    counter = 2
    while counter < 20:
        if n % counter == 0:
            counter += 1
            continue
        n += 2520
        counter = 2
    return n


print(least_multiple())

"""
Правильное решение:
    Да вроде более менее и такое, но нормальное:
    from fractions import gcd
    def lcm(a, b): # функція найменшого кратного (lcm(6, 4) = 12)
        return a / gcd(a, b) * b # gcd() - найбільший спільний дільник (не найменше кратне!!!) (gcd(6, 4) = 2)
    res = 1
    for i in range(2, 20):
        res = lcm(res, i)
    print('Это число', res)
"""

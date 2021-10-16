def difference_squares():
    n1 = 0
    n2 = 0
    for i in range(1, 101):
        n1 += i**2
        n2 += i
    n2 **= 2
    return n1 - n2


print(difference_squares())

"""
Правильное решение:
    Да вроде более менее и такое, но нормальное:
    lister = [i**2 for i in range(101)]
    lister2 = [i for i in range(101)]
    print((sum(lister2))**2 - sum(lister))
"""

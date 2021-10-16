from sympy import *


def pythagorean_triplet():
    a = 1
    b = 2
    for i in range(a, 1000):
        for j in range(b, 1000):
            if i < j and type(sqrt(i**2 + j**2)) == Integer and i + j + sqrt(i**2 + j**2) == 1000:
                return i * j * sqrt(i**2 + j**2)


print(pythagorean_triplet())

"""
Правильное решение:
    Да вроде более менее и такое (АХХАХАХАХАХАХАХАХАХАХ!!!!)))
"""

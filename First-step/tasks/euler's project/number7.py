def prime_number():
    counter = 0
    number = 0
    while counter <= 10001:
        number += 1
        l = [i for i in range(1, number + 1) if number % i == 0]
        if len(l) == 2:
            counter += 1
    return number


print(prime_number())

"""
Правильное решение:
    Да вроде более менее и такое
"""

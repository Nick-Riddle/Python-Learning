def sum_of_primes():
    number = 2
    sum = 0
    counter = 0
    while number != 2*10**6:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                counter += 1
                break
        if counter == 0:
            sum += number
        else:
            counter = 0
        print(number)
        number += 1
    else:
        return sum


print(sum_of_primes())

"""
Правильное решение:
    Да вроде более менее и такое (АХХАХАХАХАХАХАХАХАХАХ!!!!)))
"""

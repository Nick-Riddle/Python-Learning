def sum_three_five(number):
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            number += i
    return number


number = 0
print(sum_three_five(number))

"""
Правильное решение:
l = [x for x in range(1000) if x % 3 == 0 or x % 5 == 0]
print(sum(l))
"""

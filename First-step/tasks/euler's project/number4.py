def palindrome_number():
    l = []
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if str(i*j) == str(i*j)[::-1]:
                l.append(i*j)
    return max(l)


print(palindrome_number())

"""
Правильное решение:
    Да вроде более менее и такое
"""

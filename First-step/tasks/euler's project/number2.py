def fibonnacci_number(l):
    s = 0
    for i in l:
        if l[-1] % 2 == 0:
            s += l[-1]
        if l[-1] >= 4000000:
            break
        l.append(i + l[l.index(i) + 1])
    return s


print(fibonnacci_number([1, 2]))

"""
Правильное решение:
s, a, b = 0, 1, 2
while b < 4*10**6:
    if b % 2 == 0:
        s += b
    a, b = b, a + b   

print(s)
"""

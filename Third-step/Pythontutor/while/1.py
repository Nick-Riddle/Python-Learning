n, lst = int(input()), []
while n != 0:
    lst.append(n)
    n = int(input())
lst.remove(max(lst))
print(max(lst))

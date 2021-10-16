n, lst = int(input()), []
while n != 0:
    lst.append(n)
    n = int(input())
maximum = max(lst)
print(sum([1 for i in lst if i == maximum]))

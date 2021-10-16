a, lst, counter1, counter2 = int(input()), [0, 1], 0, 1
while lst[-1] <= a:
    lst.append(lst[counter1] + lst[counter2])
    counter1 += 1
    counter2 += 1
if a in lst:
    print(lst.index(a))
else:
    print(-1)



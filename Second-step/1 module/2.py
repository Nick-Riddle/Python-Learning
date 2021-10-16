objects = [1, True, False, True, False, 1, 2, [1, 2], {3: 4}, "asda", 0]
lst = []
for i in objects:
    if id(i) not in lst:
        lst.append(id(i))
print(len(lst))

# print(len({id(x) for x in objects}))

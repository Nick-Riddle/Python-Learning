def count(array):
    if not array:
        return 0
    else:
        return 1 + count(array[1:])


result = count([1, 2, 3])
print(result)

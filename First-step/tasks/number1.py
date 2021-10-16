def summer(array):
    if not array:
        return 0
    else:
        return array.pop() + summer(array)


result = summer([1, 2, 3])
print(result)

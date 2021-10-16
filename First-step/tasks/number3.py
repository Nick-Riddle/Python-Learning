def maximum(array):
    max = array[0]
    if len(array) > 1 and max < array[1]:
        return maximum(array[1:])
    else:
        while array and max >= array[0]:
            array.pop(0)
        if not array:
            return max
        return maximum(array)


"""
Правильная версия:

def maximum(array):
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub_max = maximum(array[1:])
    return array[0] if array[0] > sub_max else sub_max
"""
result = maximum([1, 2, 3, 2, 4, 3])
print(result)

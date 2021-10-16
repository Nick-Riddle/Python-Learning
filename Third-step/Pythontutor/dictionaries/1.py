lst = input().split()
dictionary = dict(zip(lst, [0 for i in range(len(lst))]))
for item in lst:
    print(dictionary[item], end=' ')
    dictionary[item] += 1


'''
counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
'''
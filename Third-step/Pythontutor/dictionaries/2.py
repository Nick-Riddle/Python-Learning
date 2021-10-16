n = int(input())
dictionary = dict(list(tuple(input().split()) for i in range(n)))
word = str(input())
for key, value in dictionary.items():
    if key == word:
        print(dictionary[key])
        break
    elif value == word:
        print(key)
        break


'''
n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])
'''
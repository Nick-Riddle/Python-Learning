dictionary = {}
for i in range(int(input())):
    for word in input().split():
        dictionary[word] = dictionary.get(word, 0) + 1
for word, quantity in sorted(dictionary.items()):
    if quantity == max(list(dictionary.values())):
        print(word)
        break


'''
counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1
         
max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))
'''
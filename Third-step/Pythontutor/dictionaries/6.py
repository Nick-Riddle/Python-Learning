dictionary = {}
sorted_dict = []
for i in range(int(input())):
    for word in input().split():
        dictionary[word] = dictionary.get(word, 0) + 1
for word, quantity in dictionary.items():
    sorted_dict.append((-quantity, word))
for i in sorted(sorted_dict):
    print(i[1])


'''
from collections import Counter
 
words = []
for _ in range(int(input())):
    words.extend(input().split())
 
counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print('\n'.join(words))
'''
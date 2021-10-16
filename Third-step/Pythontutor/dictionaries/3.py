dictionary = {}
for i in range(int(input())):
    elector, votes = input().split()
    if elector not in dictionary:
        dictionary[elector] = int(votes)
    else:
        dictionary[elector] += int(votes)
for i in sorted(list(dictionary.keys())):
    print(i, dictionary[i])


'''
num_votes = {}
for _ in range(int(input())):
    candidate, votes = input().split()
    num_votes[candidate] = num_votes.get(candidate, 0) + int(votes)
 
for candidate, votes in sorted(num_votes.items()):
    print(candidate, votes)
'''

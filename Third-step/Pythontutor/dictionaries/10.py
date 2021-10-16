from collections import defaultdict
from sys import stdin


dictionary = defaultdict(dict)
for line in stdin.readlines():
    client, thing, quantity = line.split()
    dictionary[client][thing] = dictionary[client].get(thing, 0) + int(quantity)
for client in sorted(dictionary.keys()):
    print('{}:'.format(client))
    for thing in sorted(dictionary[client].keys()):
        print(thing, dictionary[client][thing])


'''
from collections import defaultdict
from sys import stdin
 
clients = defaultdict(lambda: defaultdict(int))
for line in stdin.readlines():
    client, thing, value = line.split()
    clients[client][thing] += int(value)
         
for client in sorted(clients):
    print(client + ':')
    for thing in sorted(clients[client]):
        print(thing, clients[client][thing])
'''

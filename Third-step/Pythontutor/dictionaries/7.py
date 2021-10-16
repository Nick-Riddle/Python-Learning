dictionary = {}
for i in range(int(input())):
    country, *cities = input().split()
    dictionary[country] = tuple(cities)
for i in range(int(input())):
    city = input()
    for country, cities in dictionary.items():
        if city in cities:
            print(country)


'''
motherland = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        motherland[city] = country
         
for i in range(int(input())):
    print(motherland[input()])
'''


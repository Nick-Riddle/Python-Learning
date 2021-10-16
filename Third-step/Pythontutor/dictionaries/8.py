dictionary, new_dictionary = {}, {}
for i in range(int(input())):
    lst = input().replace('-', '').replace(',', '').split()
    dictionary[lst[0]] = lst[1:]
for key, values in dictionary.items():
    for value in values:
        new_dictionary[value] = new_dictionary.get(value, []) + [key]
print(len(new_dictionary))
for item in sorted(new_dictionary.keys()):
    print(item, '-', ', '.join(new_dictionary[item]))


'''
from collections import defaultdict
 
latin_to_english = defaultdict(list)
for i in range(int(input())):
    english_word, latin_translations_chunk = input().split(' - ')
    latin_translations = latin_translations_chunk.split(', ')
    for latin_word in latin_translations:
        latin_to_english[latin_word].append(english_word)
     
print(len(latin_to_english))
for latin_word, english_translations in sorted(latin_to_english.items()):
    print(latin_word + ' - ' + ', '.join(english_translations))
'''
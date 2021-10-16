def capitalize(word):
    return chr(ord(word[0]) - 32) + word[1:]


print(' '.join([capitalize(i) for i in str(input()).split()]))

'''
def capitalize(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]
 
source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))
'''

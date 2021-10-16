n = int(input())
main_mass = set(range(1, n + 1))
while True:
    temp = input()
    if temp == 'HELP':
        break
    temp = set(map(int, temp.split()))
    word = input()
    if word == 'YES':
        main_mass &= temp
    else:
        main_mass -= temp
print(' '.join(map(str, sorted(main_mass))))


'''
n = int(input())
all_nums = set(range(1, n + 1))
possible_nums = all_nums
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    answer = input()
    if answer == 'YES':
        possible_nums &= guess
    else:
        possible_nums &= all_nums - guess
 
print(' '.join([str(x) for x in sorted(possible_nums)]))
'''

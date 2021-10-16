languages = [{input() for j in range(int(input()))} for i in range(int(input()))]
print(str(len(set.intersection(*languages))), *sorted(set.intersection(*languages)), str(len(set.union(*languages))), *sorted(set.union(*languages)), sep='\n')


'''
students = [{input() for j in range(int(input()))} for i in range(int(input()))]
known_by_everyone, known_by_someone = set.intersection(*students), set.union(*students)
print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
print(len(known_by_someone), *sorted(known_by_someone), sep='\n')
'''

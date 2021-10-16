def recursion(person):
    if person not in dictionary:
        return []
    else:
        return [dictionary[person]] + recursion(dictionary[person])


dictionary = {}
for i in range(int(input()) - 1):
    child, parent = input().split()
    dictionary[child] = parent
for i in range(int(input())):
    person_1, person_2 = input().split()
    parents_1 = [person_1] + recursion(person_1)
    for parent_2 in [person_2] + recursion(person_2):
        if parent_2 in parents_1:
            print(parent_2)
            break


'''
def ancestors(child, p_tree):
    result = []
    result.append(child)
    while child in p_tree:
        child = p_tree[child]
        result.append(child)
    return result
 
p_tree = dict()
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent
     
m = int(input())
for i in range(m):
    child_1, child_2 = input().split()
    ancestors_for_1 = set(ancestors(child_1, p_tree))
    for ancestor in ancestors(child_2, p_tree):
        if ancestor in ancestors_for_1:
            print(ancestor)
            break
'''

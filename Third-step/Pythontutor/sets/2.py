print(' '.join(map(str, sorted(list(set(map(int, input().split())) & set(map(int, input().split())))))))

'''
print(*sorted(set(input().split()) & set(input().split()), key=int))
'''
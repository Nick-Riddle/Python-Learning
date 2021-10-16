n, m = map(int, input().split())
ann, bor = set(int(input()) for i in range(n)), set(int(input()) for j in range(m))
print('{}\n{}\n{}\n{}\n{}\n{}'.format(str(len(ann & bor)), ' '.join(map(str, sorted(ann & bor))), str(len(ann - bor)),
                                      ' '.join(map(str, sorted(ann - bor))), str(len(bor - ann)),
                                      ' '.join(map(str, sorted(bor - ann)))))

'''
def print_set(some_set):
    print(len(some_set))
    print(*[str(item) for item in sorted(some_set)])
 
N, M = [int(s) for s in input().split()]
A_colors, B_colors = set(), set()
for i in range(N):
    A_colors.add(int(input()))
for i in range(M):
    B_colors.add(int(input()))
     
print_set(A_colors & B_colors)
print_set(A_colors - B_colors)
print_set(B_colors - A_colors)
'''

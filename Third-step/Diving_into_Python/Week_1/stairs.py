import sys

for i in range(1, int(sys.argv[1]) + 1):
    print(' ' * (int(sys.argv[1]) - i) + '#' * i)

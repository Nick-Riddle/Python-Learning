import sys

print(f'{(-int(sys.argv[2]) + (int(sys.argv[2])**2 - 4*int(sys.argv[1])*int(sys.argv[3])) ** 0.5) / (2 * int(sys.argv[1]))}\n{(-int(sys.argv[2]) - (int(sys.argv[2])**2 - 4*int(sys.argv[1])*int(sys.argv[3])) ** 0.5) / (2 * int(sys.argv[1]))}')

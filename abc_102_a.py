from sys import stdin

N = int(stdin.readline().rstrip())

if N % 2 == 0:
    print(N)
else:
    print(2 * N)

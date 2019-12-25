from sys import stdin

N = int(stdin.readline().rstrip())

if N % 2 == 0:
    print(N // 2 - 1)
else:
    print(N // 2)

from sys import stdin
N = int(stdin.readline().rstrip())
if N == 1:
    print('Hello World')
else:
    A, B = [int(stdin.readline().rstrip()) for _ in range(N)]
    print(A + B)

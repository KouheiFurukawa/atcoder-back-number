from sys import stdin

N, D = [int(x) for x in stdin.readline().rstrip().split()]
if N % (2 * D + 1) == 0:
    print(N // (2 * D + 1))
else:
    print(N // (2 * D + 1) + 1)

from sys import stdin

D, N = [int(x) for x in stdin.readline().rstrip().split()]

if N == 100:
    print(101 * 100 ** D)
else:
    print(N * 100 ** D)

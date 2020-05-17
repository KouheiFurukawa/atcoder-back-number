from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]
H = [int(x) for x in stdin.readline().rstrip().split()]

H.sort()

if N <= K:
    print(0)
else:
    print(sum(H[:N - K]))

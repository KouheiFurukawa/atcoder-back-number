from sys import stdin

A, B = [int(x) for x in stdin.readline().rstrip().split()]

if A <= 9 and B <= 9:
    print(A * B)
else:
    print(-1)
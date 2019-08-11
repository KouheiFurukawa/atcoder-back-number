from sys import stdin

A, B, C = [int(x) for x in stdin.readline().rstrip().split()]

if B + C - A < 0:
    print(0)
else:
    print(B + C - A)

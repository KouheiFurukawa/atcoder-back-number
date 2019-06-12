from sys import stdin

A, B = [int(x) for x in stdin.readline().rstrip().split()]

print((A - 1) * (B - 1))

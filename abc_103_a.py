from sys import stdin

A = [int(x) for x in stdin.readline().rstrip().split()]

A.sort()

print(A[2] - A[0])

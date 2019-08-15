from sys import stdin

A, B = [int(x) for x in stdin.readline().rstrip().split()]
print(max(A + B, A - B, A * B))

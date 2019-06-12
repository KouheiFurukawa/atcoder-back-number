from sys import stdin

N, i = [int(x) for x in stdin.readline().rstrip().split()]

print(N + 1 - i)

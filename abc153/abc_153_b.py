from sys import stdin

H, N = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]

if sum(A) >= H:
    print('Yes')
else:
    print('No')

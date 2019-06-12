from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]

if N % K == 0:
    print('0')
else:
    print('1')

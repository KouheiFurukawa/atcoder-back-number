from sys import stdin

K, X = [int(x) for x in stdin.readline().rstrip().split()]

if K * 500 >= X:
    print('Yes')
else:
    print('No')

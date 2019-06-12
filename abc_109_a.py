from sys import stdin

A, B = [int(x) for x in stdin.readline().rstrip().split()]

if A % 2 == 1 and B % 2 == 1:
    print('Yes')
else:
    print('No')

from sys import stdin

A, B = [int(x) for x in stdin.readline().rstrip().split()]

if (A + B) % 2 == 0:
    print((A + B) // 2)
else:
    print('IMPOSSIBLE')

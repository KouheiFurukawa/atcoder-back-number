from sys import stdin
A, B = [int(x) for x in stdin.readline().rstrip().split()]
C, D = [int(x) for x in stdin.readline().rstrip().split()]

if B + 1 != D:
    print(1)
else:
    print(0)

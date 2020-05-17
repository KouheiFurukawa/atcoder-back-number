from sys import stdin

S, T = stdin.readline().rstrip().split()
A, B = [int(x) for x in stdin.readline().rstrip().split()]
U = stdin.readline().rstrip()

if S == U:
    print(*[A - 1, B])
else:
    print(*[A, B - 1])

from sys import stdin

X, A = [int(x) for x in stdin.readline().rstrip().split()]
if X < A:
    print(0)
else:
    print(10)

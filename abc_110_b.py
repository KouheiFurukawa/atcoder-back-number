from sys import stdin

N, M, X, Y = [int(x) for x in stdin.readline().rstrip().split()]
x = sorted([int(x) for x in stdin.readline().rstrip().split()], reverse=True)
y = sorted([int(x) for x in stdin.readline().rstrip().split()])
if y[0] > x[0] and Y > x[0] and X < y[0]:
    print('No War')
else:
    print('War')

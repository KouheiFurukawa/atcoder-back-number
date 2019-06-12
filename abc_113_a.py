from sys import stdin
X, Y = [int(x) for x in stdin.readline().rstrip().split()]
print(X + int(Y / 2))

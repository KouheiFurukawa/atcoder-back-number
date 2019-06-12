from sys import stdin
A = [int(x) for x in stdin.readline().rstrip().split()]
A.sort()
print(int(A[0] * A[1] / 2))

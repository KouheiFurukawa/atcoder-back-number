from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]

A.sort()

for i in range(N - 1):
    if A[i] != A[i + 1]:
        continue
    else:
        print('NO')
        exit()

print('YES')

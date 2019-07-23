from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(stdin.readline().rstrip()) for _ in range(N)]

first = 0
second = -1

for k in range(N):
    if A[k] > first:
        second = first
        first = A[k]
    elif second < A[k] <= first:
        second = A[k]

for l in range(N):
    if A[l] == first:
        print(second)
    else:
        print(first)

from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]

for k in range(N):
    A[k] -= k

A.sort()


def get_pity_sum(x):
    pity_sum = 0
    for l in A:
        if A[x] - l >= 0:
            pity_sum += A[x] - l
        else:
            pity_sum += l - A[x]
    return pity_sum


if N % 2 == 1:
    c = get_pity_sum(int((N - 1) / 2))
    if N == 1:
        print(c)
    else:
        print(min(c, get_pity_sum(int((N - 1) / 2 - 1)), c + (A[int((N - 1) / 2) + 1] - A[int((N - 1) / 2)]) * 2, c + (A[int((N - 1) / 2)] - A[int((N - 1) / 2 - 1)]) * 2))
else:
    d = get_pity_sum(int(N / 2))
    print(min(get_pity_sum(int(N / 2)), d + (A[int(N / 2) + 1] - A[int(N / 2)]) * 2))

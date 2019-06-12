from sys import stdin
N, K = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]

X = A[0]
index = 0
cnt = 0

while index < N:
    end_index = min(index + K, N)
    sub = [A[x] for x in range(index, end_index)]
    flag = 0
    for k in range(len(sub)):
        if sub[k] != X:
            A[k + index] = X
            flag += 1
    if flag != 0:
        cnt += 1
    index += K - 1

print(cnt)

from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
B = [int(x) for x in stdin.readline().rstrip().split()]
cnt = 0
n = 0
current = 0

for i in range(N - 1):
    if B[i - 1] > B[i] and B[i + 1] > B[i]:
        if B[i] < A[i]:
            print(-1)
            exit()
        if (B[i] - A[i]) % (A[i - 1] + A[i + 1]) == 0:
            current = i

while n < N:
    print(A)
    if current == N - 1:
        print((B[current] - A[current]) // (A[current - 1] + A[0]))
        cnt += (B[current] - A[current]) // (A[current - 1] + A[0])
    elif current == 0:
        print((B[current] - A[current]) // (A[N - 1] + A[current + 1]))
        cnt += (B[current] - A[current]) // (A[N - 1] + A[current + 1])
    else:
        cnt += (B[current] - A[current]) // (A[current - 1] + A[current + 1])
    A[current] = B[current]
    if current == N - 2:
        if (B[current + 1] - A[current + 1]) % (A[current] + A[0]) == 0:
            current += 1
        elif (B[current - 1] - A[current - 1]) % (A[current - 2] + A[current]) == 0:
            current -= 1
        n += 1
        continue
    if current == N - 1:
        if (B[0] - A[0]) % (A[current] + A[1]) == 0:
            current = 0
        elif (B[current - 1] - A[current - 1]) % (A[current - 2] + A[current]) == 0:
            current -= 1
        n += 1
        continue
    if current == 0:
        if (B[current + 1] - A[current + 1]) % (A[current] + A[current + 2]) == 0:
            current += 1
        elif (B[N - 1] - A[N - 1]) % (A[N - 2] + A[current]) == 0:
            current = N - 1
        n += 1
        continue
    if current == 1:
        if (B[current + 1] - A[current + 1]) % (A[current] + A[current + 2]) == 0:
            current += 1
        elif (B[current - 1] - A[current - 1]) % (A[N - 1] + A[current]) == 0:
            current -= - 1
        n += 1
        continue
    if (B[current + 1] - A[current + 1]) % (A[current] + A[current + 2]) == 0:
        current += 1
    elif (B[current - 1] - A[current - 1]) % (A[current - 2] + A[current]) == 0:
        current -= 1
    n += 1
    continue

print(A)
print(cnt)

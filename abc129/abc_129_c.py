from sys import stdin

N, M = [int(x) for x in stdin.readline().rstrip().split()]
a = [int(stdin.readline().rstrip()) for _ in range(M)]
fib = [1, 1]
for k in range(N):
    fib.append((fib[-1] + fib[-2]) % 1000000007)
if M == 0:
    print(fib[N])
    exit()
ans = fib[a[0] - 1]
for l in range(M - 1):
    if a[l + 1] - a[l] == 1:
        print(0)
        exit()
    ans = ans * fib[a[l + 1] - a[l] - 2]
ans = ans * fib[N - a[-1] - 1]
print(ans % 1000000007)

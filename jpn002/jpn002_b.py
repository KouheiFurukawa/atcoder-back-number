from sys import stdin

N = int(stdin.readline().rstrip())
D = [int(x) for x in stdin.readline().rstrip().split()]

if D[0] > 0:
    print(0)
    exit()
D.sort()

ans = 1
mod = 998244353
b = 1

temp = 1
for i in range(1, N):
    if D[i] == 0:
        print(0)
        exit()
    if D[i] - D[i - 1] > 1:
        print(0)
        exit()
    if D[i] != D[i - 1]:
        b = temp
        temp = 1
    else:
        temp += 1
    ans *= b
    ans %= mod

print(ans % mod)

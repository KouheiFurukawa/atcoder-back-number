from sys import stdin

N = int(stdin.readline().rstrip())
a = [int(x) for x in stdin.readline().rstrip().split()]

ans = []
for k in reversed(range(1, N + 1)):
    if a[k - 1] == 1:
        ans.append(k)
        tmp = 1
        while tmp * tmp <= k:
            if k % tmp == 0:
                a[tmp - 1] ^= 1
                if tmp != k // tmp:
                    a[k // tmp - 1] ^= 1
            tmp += 1

x = len(ans)
print(x)
if x >= 0:
    print(*ans)

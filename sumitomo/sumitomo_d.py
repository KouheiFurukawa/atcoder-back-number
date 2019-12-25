from sys import stdin

N = int(stdin.readline().rstrip())
S = stdin.readline().rstrip()

ans = 0
num_str = [str(i).zfill(3) for i in range(1000)]

for i in num_str:
    j = 0
    k = 0
    while k < 3:
        while j < len(S):
            if S[j] == i[k]:
                k += 1
                j += 1
                break
            j += 1
        if j == len(S):
            break
    if k == 3:
        ans += 1

print(ans)

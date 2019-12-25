from sys import stdin
import math
N = int(stdin.readline().rstrip())

ans = math.floor(N / 1.08)

while True:
    if math.floor(ans * 1.08) > N:
        print(':(')
        exit()
    if math.floor(ans * 1.08) == N:
        print(ans)
        exit()
    else:
        ans += 1

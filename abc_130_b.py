from sys import stdin

N, X = [int(x) for x in stdin.readline().rstrip().split()]
L = [int(x) for x in stdin.readline().rstrip().split()]
Sum = 0
cnt = 1
for i in range(N):
    if Sum + L[i] <= X:
        cnt += 1
        Sum += L[i]
    else:
        break
print(cnt)

from sys import stdin

N = int(stdin.readline().rstrip())

XL = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(N)]
R = []
for i in range(N):
    R.append([XL[i][0] - XL[i][1], XL[i][0] + XL[i][1]])
R.sort(key=lambda x:x[1])
ans = [R[0]]

for i in range(1, N):
    if R[i][0] >= ans[-1][1]:
        ans.append(R[i])

print(len(ans))

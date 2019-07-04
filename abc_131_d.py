from sys import stdin, exit

N = int(stdin.readline().rstrip())
work = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(N)]

work.sort(key=lambda x: x[1])
time = 0
for k in range(N):
    if time + work[k][0] > work[k][1]:
        print('No')
        exit()
    time += work[k][0]
print('Yes')

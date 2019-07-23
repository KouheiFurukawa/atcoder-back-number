from sys import stdin, exit

N, K = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]

X = []
Y = []
for k in range(len(A) + 1):
    X.extend(A)
    Y.extend(A)
cnt = 0
while cnt == 0 or cnt % len(A) != 0:
    x = X[0]
    ind = 1
    while X[ind] != x:
        ind += 1
    X = X[ind + 1:]
    cnt += ind + 1

res = (N * K) % cnt
if res == 0:
    print(*[])
    exit()

Y = Y[0:res]

cc = 0
ans = []
T = [[] for _ in range(max(Y) + 1)]
while cc < res - 1:
    y = Y[0]
    index = 1
    while index < len(Y):
        if Y[index] != y:
            index += 1
        else:
            break
    if index != len(Y):
        Y = Y[index + 1:]
        cc += index + 1
    else:
        ans.append(y)
        Y = Y[1:]
        cc += 1

print(*(ans + Y))

from sys import stdin
N, M = [int(x) for x in stdin.readline().rstrip().split()]
X = [int(x) for x in stdin.readline().rstrip().split()]
X.sort()
if N >= M:
    print('0')
else:
    r = []
    for i in range(M - 1):
        r.append(X[i + 1]-X[i])
    r.sort()
    print(r)
    if N != 1:
        print(sum(r[:-N+1]))
    else:
        print(sum(r))

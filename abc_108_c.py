from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]
# a+b, b+c, c+a が全部Kで割り切れる条件：a, b, c 全部Kで割り切れるor余りがK/2
if K % 2 == 0:
    a = int(N / K)
    b = int((N + K / 2) / K)
    print(a ** 3 + b ** 3)
else:
    a = int(N / K)
    print(a ** 3)

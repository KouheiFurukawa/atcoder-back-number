from sys import stdin

K = int(stdin.readline().rstrip())

if K % 2 == 1:
    print((K // 2 + 1) * (K // 2))
else:
    print(int((K / 2) ** 2))

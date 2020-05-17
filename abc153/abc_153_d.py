from sys import stdin

H = int(stdin.readline().rstrip())
cnt = 0

while H > 1:
    if H % 2 == 1:
        H = (H - 1) // 2
    else:
        H //= 2
    cnt += 1

print(2 ** (cnt + 1) - 1)

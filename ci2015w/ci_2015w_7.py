from sys import stdin

n = int(stdin.readline().rstrip())


def gen(x):
    if x == 0:
        return 1
    else:
        return (1103515245 * gen(x - 1) + 12345) % (2 ** 26)


v = gen(n) % (2 ** 10)
w = v
cnt = 0

while v != w or cnt == 0:
    w = (1103515245 * w + 12345) % (2 ** 26) % (2 ** 10)
    cnt += 1

print(cnt)

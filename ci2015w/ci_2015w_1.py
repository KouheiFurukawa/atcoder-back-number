from sys import stdin

n = int(stdin.readline().rstrip())


def gen(x):
    if x == 0:
        return 1
    else:
        return (161 * gen(x - 1) + 2457) % (2 ** 24)


print(gen(n))

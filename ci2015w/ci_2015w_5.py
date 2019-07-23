from sys import stdin

n = int(stdin.readline().rstrip())


def gen(x):
    if x == 0:
        return 1
    else:
        return (1103515245 * gen(x - 1) + 12345) % (2 ** 26)


print(gen(n))

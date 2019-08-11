x = 10


def calc(n):
    if n <= 2:
        return 1
    else:
        return calc(n - 1) + calc(n - 2)


print(calc(x))

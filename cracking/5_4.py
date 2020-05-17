def get_next(n):
    c = n
    c0 = 0
    c1 = 0
    while c & 1 == 0 and c != 0:
        c0 += 1
        c >>= 1
    while c & 1 == 1 and c != 1:
        c1 += 1
        c >>= 1

    n += 1 << (c0 + c1)

    mask = ~((1 << (c0 + c1)) - 1)
    n = n & mask
    n = n + 2 ** (c1 - 1) - 1
    print(bin(n))


if __name__ == '__main__':
    get_next(0b11011001111100)

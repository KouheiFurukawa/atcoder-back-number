def best_reverse(n):
    c = n
    prev = 0
    current = 0
    ans = 0
    while c != 0:
        b = c & 1
        if b == 1:
            current += 1
        if b == 0:
            prev = current
            current = 0
            if c >> 1 & 1 == 0:
                prev = 0
        print(current, prev)
        ans = max (ans, current + prev + 1)
        c >>= 1
    print(ans)

if __name__ == '__main__':
    best_reverse(0b110111001111)

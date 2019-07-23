n = 1
cnt = 0

while cnt != 1000000:
    n = (161 * n + 2457) % (2 ** 24)
    cnt += 1

print(n)

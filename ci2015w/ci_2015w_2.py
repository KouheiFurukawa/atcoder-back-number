def gen(x):
    if x == 0:
        return 1
    else:
        return (161 * gen(x - 1) + 2457) % (2 ** 24)


cnt = 0
for k in range(100):
    if gen(k) % 2 == 0:
        cnt += 1

print(cnt)

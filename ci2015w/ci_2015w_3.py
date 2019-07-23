def gen(x):
    if x == 0:
        return 1
    else:
        return (161 * gen(x - 1) + 2457) % (2 ** 24)


cnt = 0
for k in range(101):
    if gen(k) % 2 == 0 and k % 2 == 1:
        cnt += 1

print(cnt)

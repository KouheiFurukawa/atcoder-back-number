from sys import stdin

d = float(stdin.readline().rstrip())


def calc(P, Q, h, x, y, reverse=False):
    if not reverse:
        if y > h and (x - P) * (3 ** 0.5) + h > y and (x - Q) * (-(3 ** 0.5)) + h > y:
            return 1
        else:
            return 0
    else:
        if y < h and (x - P) * (-(3 ** 0.5)) + h < y and (x - Q) * (3 ** 0.5) + h < y:
            return 1
        else:
            return 0


c = int(10 // d + 1)
ans = 0
for k in range(11):
    for l in range(-10, 10):
        ans += calc(0, 10, 0, k, l)
        ans += 2 * calc(0, 10 / 3, 5 * (3 ** 0.5) * 2 / 3, d * k, d * l, True)
        ans += calc(10 / 3, 20 / 3, 0, d * k, d * l, True)
        ans += 2 * calc(10 / 9, 20 / 9, 0, d * k, d * l, True)
        ans += 2 * calc(10 / 9, 20 / 9, 5 * (3 ** 0.5) * 3 / 3, d * k, d * l)
        ans += 2 * calc(10 / 9, 20 / 9, 5 * (3 ** 0.5) * 8 / 9, d * k, d * l, True)
        ans += 2 * calc(10 / 9, 20 / 9, 5 * (3 ** 0.5) * (-2) / 9, d * k, d * l, True)
        ans += 2 * calc(0, 10 / 9, 5 * (3 ** 0.5) * 2 / 9, d * k, d * l)
        ans += 2 * calc(0, 10 / 9, 5 * (3 ** 0.5) * 4 / 9, d * k, d * l)

print(ans + 17)

import decimal
decimal.getcontext().prec = 32
root_5 = decimal.Decimal(1 / (5 ** 0.5))
phi = decimal.Decimal((1 + 5 ** 0.5) / 2)
power = 141
f = []


for l in range(140):
    if l == 0 or l == 1:
        f.append(1)
    else:
        f.append(f[len(f) - 1] + f[len(f) - 2])


def g(x):
    output = root_5
    for i in range(x):
        output = output * phi
    return output


ans = 0
for k in range(1, power):
    if abs(f[k - 1] - g(k)) > ans:
        print(f[k - 1], g(k), '{:.32g}'.format(abs(f[k - 1] - g(k))))
        ans = abs(f[k - 1] - g(k))

print('{:.32g}'.format(ans))
print('0' * (32 - len(str('{:.32g}'.format(ans)).replace('.', ''))) + str('{:.32g}'.format(ans)).replace('.', ''))

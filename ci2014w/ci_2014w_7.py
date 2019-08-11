import decimal
decimal.getcontext().prec = 32
phi = decimal.Decimal((1 + 5 ** 0.5) / 2)
ans = decimal.Decimal(1 / (5 ** 0.5))
power = 140

for i in range(power):
    ans = ans * phi

print('{:.32g}'.format(ans))

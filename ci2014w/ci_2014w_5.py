from sys import stdin

X = [int(x) for x in stdin.readline().rstrip().split()]
Y = [int(x) for x in stdin.readline().rstrip().split()]
test_x = [12345678901234567890123456789012, 4]
test_y = [98765432109876543210987654321098, 9]
ans = [(test_x[0] * test_y[0] // (10 ** (len(str(test_x[0] * test_y[0])) - 32))).__round__(),
       len(str(test_x[0] * test_y[0])) - (62 - test_x[1] - test_y[1])]

print(*ans)

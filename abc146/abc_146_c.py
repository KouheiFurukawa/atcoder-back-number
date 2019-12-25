from sys import stdin

A, B, X = [int(x) for x in stdin.readline().rstrip().split()]

if A + B > X:
    print(0)
    exit()
ans = 1
digits = 1
while ans * 10 * A + (digits + 1) * B <= X:
    ans *= 10
    digits += 1

ans = ans + min((X - (ans * A + digits * B)) // A, 9 * ans - 1)

print(min(ans, 1000000000))

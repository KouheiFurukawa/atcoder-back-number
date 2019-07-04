from sys import stdin

A, B = [int(x) for x in stdin.readline().rstrip().split()]
k = 1
bit_sum = []


def bit(x, n):
    return 2 ** (n - 1) * ((x + 1) // (2 ** n)) + max(0, (x + 1) % (2 ** n) - 2 ** (n - 1))


while 2 ** (k - 1) <= B:
    bit_sum.append(bit(B, k) - bit(A - 1, k))
    k += 1

ans = [(bit_sum[k] % 2) * 2 ** k for k in range(len(bit_sum))]
print(sum(ans))

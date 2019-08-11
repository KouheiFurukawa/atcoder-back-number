from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]
div = []
A_sum = sum(A)
i = 1
while i ** 2 < A_sum:
    if A_sum % i == 0:
        div.append(i)
        div.append(A_sum // i)
    i += 1

div.sort(reverse=True)

for j in div:
    mod = [a % j for a in A]
    mod.sort()
    s = sum(mod)
    if sum(mod[:-s // j]) <= K:
        print(j)
        break

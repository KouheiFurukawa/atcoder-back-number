from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]

min_number = 10 ** 10
max_number = 0

for k in A:
    if k > max_number:
        max_number = k
    if k < min_number:
        min_number = k

print(max_number - min_number)

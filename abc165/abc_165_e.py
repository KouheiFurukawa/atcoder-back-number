from sys import stdin

N, M = [int(x) for x in stdin.readline().rstrip().split()]

head = 1
tail = N

while head <= M:
    if (N % 2 == 0 and tail - head == N // 2) or (N % 4 == 0 and tail - head == N // 2 - 1):
        tail -= 1
    print(head, tail)
    head += 1
    tail -= 1

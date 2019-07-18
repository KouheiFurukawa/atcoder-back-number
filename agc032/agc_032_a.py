from sys import stdin, exit
from collections import deque

N = int(stdin.readline().rstrip())
b = [int(x) for x in stdin.readline().rstrip().split()]
ans = deque([])

while N > 0:
    index = N - 1
    while index >= 0:
        if b[index] == index + 1:
            ans.appendleft(b[index])
            b1 = b[:index]
            b2 = b[index + 1:]
            b = b1 + b2
            N -= 1
            break
        index -= 1
        if index == -1:
            print(-1)
            exit()

print(*ans)

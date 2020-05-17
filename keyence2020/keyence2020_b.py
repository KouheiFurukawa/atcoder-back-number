from sys import stdin
import math

H = int(stdin.readline().rstrip())
W = int(stdin.readline().rstrip())
N = int(stdin.readline().rstrip())

print(math.ceil(N / max(H, W)))

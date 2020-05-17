from sys import stdin
import math

H, A = [int(x) for x in stdin.readline().rstrip().split()]

print(math.ceil(H / A))

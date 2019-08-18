from sys import stdin

P, Q, R = [int(x) for x in stdin.readline().rstrip().split()]
print(min(P + Q, Q + R, R + P))

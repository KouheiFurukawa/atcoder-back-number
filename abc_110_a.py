from sys import stdin

N = [int(x) for x in stdin.readline().rstrip().split()]
N.sort(reverse=True)
print(N[0] * 10 + N[1] + N[2])

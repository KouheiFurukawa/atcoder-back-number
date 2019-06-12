from sys import stdin
N = int(stdin.readline().rstrip())
T, A = [int(x) for x in stdin.readline().rstrip().split()]
H = [int(x) for x in stdin.readline().rstrip().split()]
temperature = [abs(T - x * 0.006 - A) for x in H]
ST = sorted(temperature)
print(temperature.index(ST[0]) + 1)

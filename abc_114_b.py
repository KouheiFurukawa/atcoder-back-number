from sys import stdin
S = stdin.readline().rstrip()
A = [abs(int(S[k:k+3]) - 753) for k in range(len(S) - 2)]
A.sort()
print(A[0])

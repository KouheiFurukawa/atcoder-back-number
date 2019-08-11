S = open('../sample.txt').readlines()

S = [s.replace('\n', '') for s in S]
first = []
ans = []

for n in range(len(S)):
    if S[n] not in first:
        first.append(S[n])
    elif S[n] not in ans:
        ans.append(S[n])

for x in first:
    if x in ans:
        print(x)

print(len(ans))

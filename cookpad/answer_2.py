from sys import stdin

S = stdin.readline().rstrip()

start = 0
end = 0

for i in range(len(S)):
    if S[i] == '{':
        start = i
    elif S[i] == '}':
        end = i

ans = []
brace = S[start + 1:end].split(',')

for b in brace:
    ans.append(S[:start] + b + S[end + 1:])
print(*ans)

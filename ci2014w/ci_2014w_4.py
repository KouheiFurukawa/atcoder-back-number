x = 140

ans = []

for i in range(x):
    if i == 0 or i == 1:
        ans.append(x)
    else:
        ans.append(ans[len(ans) - 1] + ans[len(ans) - 2])

print(ans[x - 1])

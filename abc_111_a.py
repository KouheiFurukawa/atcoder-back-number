from sys import stdin

n = stdin.readline().rstrip()
output = ''
for k in n:
    if k == '1':
        output += '9'
    else:
        output += '1'
print(output)

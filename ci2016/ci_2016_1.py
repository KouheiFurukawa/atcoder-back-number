from sys import stdin
import codecs

emoji = [
    ['****', '|  |', '*  *', '|  |', '****'],
    ['*', '|', '*', '|', '*'],
    ['****', '   |', '****', '|   ', '****'],
    ['****', '   |', '****', '   |', '****'],
    ['*  *', '|  |', '****', '   |', '   *'],
    ['****', '|   ', '****', '   |', '****'],
    ['*   ', '|   ', '****', '|  |', '****'],
    ['****', '   |', '   *', '   |', '   *'],
    ['****', '|  |', '****', '|  |', '****'],
    ['****', '|  |', '****', '   |', '   *']
]

N = stdin.readline().rstrip()
result = []
for l in range(5):
    line = ''
    for i in range(len(N)):
        line += emoji[int(N[i])][l]
        if i != len(N) - 1:
            line += '  '
    print(line)
    result.append(line)

print(*result, sep="\n", file=codecs.open('out1.txt', 'w', 'utf-8'))

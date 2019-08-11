from sys import stdin
import codecs

i = [int(x) for x in stdin.readline().rstrip().split(',')]
place = []
lines = []
result = []

emoji = [
    ['*|*|*', '*   *', '*   *', '*|*|*'],
    ['*|*|*'],
    ['* *|*', '* * *', '* * *', '*|* *'],
    ['* * *', '* * *', '* * *', '*|*|*'],
    ['*|* *', '  *  ', '  *  ', '*|*|*'],
    ['*|* *', '* * *', '* * *', '* *|*'],
    ['*|*|*', '  * *', '  * *', '  *|*'],
    ['*    ', '*    ', '*    ', '*|*|*'],
    ['*|*|*', '* * *', '* * *', '*|*|*'],
    ['*|*  ', '* *  ', '* *  ', '*|*|*'],
]

for k in range(int(len(i) // 2)):
    if k == 0:
        place.append([0, i[1]])
    else:
        place.append([i[2 * k], i[2 * k + 1]])
        lines.append(i[2 * k + 1])
line_num = 4 + max(lines)
num = str(i[0])

for n in range(len(num)):
    for q in range(place[n][0]):
        result.append(' ' * (line_num + 1))
    for r in range(len(emoji[int(num[n])])):
        result.append(' ' * place[n][1] + emoji[int(num[n])][r] + ' ' * (line_num - place[n][1] - 4))

output = ['' for k in range(line_num + 1)]

for t in range(len(result)):
    for u in range(len(result[t])):
        output[u] += result[t][u]

print(*output, sep="\n", file=codecs.open('out3.txt', 'w', 'utf-8'))
for x in range(len(output)):
    print(output[x])

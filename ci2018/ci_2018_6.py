from sys import stdin
from ci2018 import ci_2018_5
import codecs

input_k = int(stdin.readline().rstrip())
input_data = [int(x) for x in open('image2.txt').readlines()[0].split()]

subs = ci_2018_5.clustering(input_k, input_data)
w = int((len(input_data) // 3) ** 0.5)
print(w)


def to_8_bit(s):
    output = 0
    for i in range(len(s)):
        output += int(s[i]) * 2 ** (8 - i)
    return output


def to_binary(i):
    output = ''
    n = 31
    while n >= 0:
        if i >= 2 ** n:
            output = str(output) + '1'
            i -= 2 ** n
        else:
            output = str(output) + '0'
        n -= 1
    return str(to_8_bit(output[24:32])) + ' ' \
        + str(to_8_bit(output[16:24])) + ' ' \
        + str(to_8_bit(output[8:16])) + ' ' \
        + str(to_8_bit(output[:8]))


tif = '77 77 0 42 0 0 0 8 0 7 1 0 0 4 0 0 0 1 ' + to_binary(w) + ' 1 1 0 4 0 0 0 1 ' + to_binary(w) \
      + ' 1 2 0 3 0 0 0 3 0 0 0 98 1 6 0 3 0 0 0 1 0 2 0 0 1 17 0 4 0 0 0 1 0 0 0 104 1 21 0 3 0 0 0 1 0 3 0 0 1 23 ' \
        '0 4 0 0 0 1 ' + to_binary(w ** 2 * 3) + ' 0 0 0 0 0 8 0 8 0 8 '

pixels = [input_data[3 * x:3 * x + 3] for x in range(len(input_data) // 3)]

for pixel in pixels:
    d = 10 ** 8
    n = 0
    for j in range(input_k):
        dr = abs(pixel[0] - subs[j][0])
        dg = abs(pixel[1] - subs[j][1])
        db = abs(pixel[2] - subs[j][2])
        if dr + dg + db <= d:
            n = j
            d = dr + dg + db
    tif += str(subs[n][0]) + ' ' + str(subs[n][1]) + ' ' + str(subs[n][2]) + ' '

print(tif, file=codecs.open('out.txt', 'w', 'utf-8'))

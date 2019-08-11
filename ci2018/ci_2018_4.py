from sys import stdin

k = int(stdin.readline().rstrip())
data = [int(x) for x in open('image2.txt').readlines()[0].split()]
pixels = [data[3 * x:3 * x + 3] for x in range(len(data) // 3)]

brightness = [(
    pixels[i][0] ** 2 + pixels[i][1] ** 2 + pixels[i][2] ** 2, i, (pixels[i][0], pixels[i][1], pixels[i][2])
) for i in range(len(pixels))]
brightness.sort(key=lambda x: (x[0], -x[1]))

print(brightness)

for i in range(k):
    print(brightness[len(brightness) * i // k][1])
    print(brightness[len(brightness) * i // k][2])

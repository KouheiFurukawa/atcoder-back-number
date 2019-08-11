data = [int(x) for x in open('image1.txt').readlines()[0].split()]

pixels = [data[3 * x:3 * x + 3] for x in range(len(data) // 3)]
ans = 0
print(pixels)
while pixels[ans] != [255, 255, 255]:
    ans += 1

print(ans + 1)

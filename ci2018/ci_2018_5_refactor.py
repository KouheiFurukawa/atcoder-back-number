from sys import stdin


def clustering(k, data):
    pixels = [data[3 * x:3 * x + 3] for x in range(len(data) // 3)]

    brightness = [(
        pixels[i][0] ** 2 + pixels[i][1] ** 2 + pixels[i][2] ** 2, i, [pixels[i][0], pixels[i][1], pixels[i][2]]
    ) for i in range(len(pixels))]
    brightness.sort(key=lambda x: (x[0], -x[1]))
    subs = [brightness[len(brightness) * i // k][2] for i in range(k)]

    for _ in range(10):
        cluster = [[] for _ in range(k)]

        for pixel in pixels:
            d = 10 ** 8
            n = 0
            for j in range(k):
                dr = abs(pixel[0] - subs[j][0])
                dg = abs(pixel[1] - subs[j][1])
                db = abs(pixel[2] - subs[j][2])
                if dr + dg + db <= d:
                    n = j
                    d = dr + dg + db
            cluster[n].append(pixel)

        subs = []

        for i in range(k):
            pxl_cnt = len(cluster[i])
            ave = [sum([px[0] for px in cluster[i]]) // pxl_cnt,
                   sum([px[1] for px in cluster[i]]) // pxl_cnt,
                   sum([px[2] for px in cluster[i]]) // pxl_cnt]
            new = 0
            new_d = 10 ** 8
            for l in range(len(cluster[i])):
                new_dr = abs(ave[0] - cluster[i][l][0])
                new_dg = abs(ave[1] - cluster[i][l][1])
                new_db = abs(ave[2] - cluster[i][l][2])
                if new_db + new_dr + new_dg <= new_d:
                    new = l
                    new_d = new_db + new_dr + new_dg
            subs.append(cluster[i][new])

    return subs


if __name__ == "__main__":
    input_k = int(stdin.readline().rstrip())
    input_data = [int(x) for x in open('image2.txt').readlines()[0].split()]
    print(clustering(input_k, input_data))

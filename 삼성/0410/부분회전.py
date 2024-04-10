arr = [[7 * i + j for j in range(1, 7)] for i in range(7)]
new_arr = [[0 for _ in range(7)] for _ in range(7)]
sy, sx = 2, 2
length = 3

for cow in arr:
    print(cow)

def rotate_90(sy, sx, length):
    global arr, new_arr
    for y in range(sy, sy + length):
        for x in range(sx, sx + length):
            oy, ox = y - sy, x - sx
            ry, rx = ox, length - 1 - oy
            new_arr[ry + sy][rx + sx] = arr[y][x]

    for y in range(sy, sy + length):
        for x in range(sx, sx + length):
            arr[y][x] = new_arr[y][x]
rotate_90(2, 2, 3)
for cow in arr:
    print(cow)

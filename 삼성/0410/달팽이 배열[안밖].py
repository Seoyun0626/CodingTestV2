arr = [[0] * 5 for _ in range(5)]
d = [[0, -1], [1, 0], [0, 1], [-1, 0]]

def tornado():
    y = len(arr) // 2
    x = len(arr) // 2
    dist = 1
    d_idx = 0
    num = 0
    move_cnt = 0

    while True:
        for _ in range(dist):
            dy = d[d_idx][0]
            dx = d[d_idx][1]
            y = y + dy
            x = x + dx
            if x == -1 and y == 0:
                return
            num += 1
            arr[y][x] = num
        move_cnt += 1
        d_idx = (d_idx + 1) % 4

        if move_cnt == 2:
            move_cnt = 0
            dist += 1
tornado()

for cow in arr:
    print(cow)


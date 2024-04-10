arr = [[0] * 5 for _ in range(5)]
d = [[0, -1], [1, 0], [0, 1], [-1, 0]]

def tornado():
    global arr
    y = len(arr) // 2
    x = len(arr) // 2
    d_idx = 0
    move_cnt = 0
    dist = 1
    num = 0

    while True:
        for _ in range(dist):
            dy, dx = d[d_idx]
            y = y + dy
            x = x + dx
            if y == 0 and x == -1:
                return
            num += 1
            arr[y][x] = num
        d_idx = (d_idx + 1) % 4
        move_cnt += 1

        if move_cnt == 2:
            move_cnt = 0
            dist += 1

tornado()
for cow in arr:
    print(cow)






# 안 -> 밖으로
arr = [[0] * 5 for _ in range(5)]

def tornado():
    global arr
    d = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 서, 남, 동, 북
    y = len(arr) // 2
    x = len(arr) // 2
    num = 0 # 칸에 채워넣을 값
    dist = 1
    d_idx = 0 # 서, 남, 동, 북
    move_count = 0 # 2가 되면 dist길이가 1 늘어나고 move_count는 다시 0 초기화
    while True:
        for _ in range(dist):
            dy, dx = d[d_idx]
            Y = y + dy
            X = x + dx
            if (Y, X) == (0, -1): # 0행 -1열이 토네이도가 모두 끝나고 나서 위치
                return
            num += 1
            arr[Y][X] = num
            y = Y
            x = X
        move_count += 1
        d_idx = (d_idx + 1) % 4
        if move_count == 2:
            dist += 1
            move_count = 0
tornado()
for cow in arr:
    print(cow)


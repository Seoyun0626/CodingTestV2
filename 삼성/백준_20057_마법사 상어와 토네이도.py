d = [[0, -1], [1, 0], [0, 1], [-1, 0]]

tornado = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]
tornado_90 = list(map(list, zip(*tornado[::-1])))
tornado_180 = [tmp[::-1] for tmp in tornado]
tornado_270 = [tmp[::-1] for tmp in list(map(list, zip(*tornado)))[::-1]]
# sand_print(tornado) # 왼쪽
# sand_print(tornado_90) # 위쪽
# sand_print(tornado_180) # 오른쪽
# sand_print(tornado_270) # 아래쪽

## 알파 위치
alpha = [[2, 1], [3, 2], [2, 3], [1, 2]]


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# sand_print(graph)

## 초기값 설정
y = n // 2
x = n // 2
dist = 1
move_cnt = 0
d_idx = 0
sand_out = 0
flag = 0

while True:
    dy, dx = d[d_idx]
    for _ in range(dist):
        y = y + dy
        x = x + dx
        if y == 0 and x == 0:
            flag = 1
            break
        # print("시작")
        # print("dist", dist)
        # print("y, x", y, x)
        cur_sand = graph[y][x]
        if cur_sand == 0:
            continue
        tmp_x = x - 2
        tmp_y = y - 2
        # print("토네이도 이동 후 위치", y, x, d_idx)
        # for cow in graph:
        #     print(cow)
        alpha_sand = cur_sand
        graph[y][x] = 0
        if d_idx == 0:
            for i in range(5):
                for j in range(5):
                    tmp_sand = int(tornado[i][j] * cur_sand)
                    alpha_sand -= tmp_sand
                    if 0 <= i + tmp_y < n and 0 <= j + tmp_x < n:
                        graph[i + tmp_y][j + tmp_x] += tmp_sand
                    else:
                        sand_out += tmp_sand
            alpha_y, alpha_x = alpha[0]
            if 0 <= alpha_y + tmp_y < n and 0 <= alpha_x + tmp_x < n:
                graph[alpha_y + tmp_y][alpha_x + tmp_x] += alpha_sand
            else:
                sand_out += alpha_sand
        elif d_idx == 1:
            for i in range(5):
                for j in range(5):
                    tmp_sand = int(tornado_270[i][j] * cur_sand)
                    alpha_sand -= tmp_sand
                    if 0 <= i + tmp_y < n and 0 <= j + tmp_x < n:
                        graph[i + tmp_y][j + tmp_x] += tmp_sand
                    else:
                        sand_out += tmp_sand
            alpha_y, alpha_x  = alpha[1]
            if 0 <= alpha_y + tmp_y < n and 0 <= alpha_x + tmp_x < n:
                graph[alpha_y + tmp_y][alpha_x + tmp_x] += alpha_sand
            else:
                sand_out += alpha_sand
        elif d_idx == 2:
            for i in range(5):
                for j in range(5):
                    tmp_sand = int(tornado_180[i][j] * cur_sand)
                    alpha_sand -= tmp_sand
                    if 0 <= i + tmp_y < n and 0 <= j + tmp_x < n:
                        graph[i + tmp_y][j + tmp_x] += tmp_sand
                    else:
                        sand_out += tmp_sand
            alpha_y, alpha_x = alpha[2]
            # print(alpha_y + tmp_y, alpha_x + tmp_x)
            if 0 <= alpha_y + tmp_y < n and 0 <= alpha_x + tmp_x < n:
                graph[alpha_y + tmp_y][alpha_x + tmp_x] += alpha_sand
            else:
                sand_out += alpha_sand
        elif d_idx == 3:
            for i in range(5):
                for j in range(5):
                    tmp_sand = int(tornado_90[i][j] * cur_sand)
                    alpha_sand -= tmp_sand
                    if 0 <= i + tmp_y < n and 0 <= j + tmp_x < n:
                        graph[i + tmp_y][j + tmp_x] += tmp_sand
                    else:
                        sand_out += tmp_sand
            alpha_y, alpha_x  = alpha[3]
            if 0 <= alpha_y + tmp_y < n and 0 <= alpha_x + tmp_x < n:
                graph[alpha_y + tmp_y][alpha_x + tmp_x] += alpha_sand
            else:
                sand_out += alpha_sand
        # print("나가리 모래", sand_out)
        # print("모래 흩어진 후 그래프")
        # for cow in graph:
        #     print(cow)
    move_cnt += 1
    d_idx = (d_idx + 1) % 4
    # print("다음 좌표 정보")
    # print(d_idx)
    if flag == 1:
        break
    if move_cnt == 2:
        move_cnt = 0
        dist += 1
# 0,0 일 떄 처리
cur_sand = graph[0][0]
in_sand = int(cur_sand * 0.07) + int(cur_sand * 0.02)  + int(cur_sand * 0.01)
out_sand = int(cur_sand * 0.1) * 2 + int(cur_sand * 0.07) + int(cur_sand * 0.02) + int(cur_sand * 0.05)
outalpha_sand = cur_sand - in_sand - out_sand
sand_out += (outalpha_sand + out_sand)
print(sand_out)


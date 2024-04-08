N, M, K = map(int, input().split())
move = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
info = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    # 행 열 질량 거리 방향
    r, c, m, s, d = map(int, input().split())
    info[r - 1][c - 1].append([m, s, d])

# print("맨 처음 초기 info")
# for cow in info:
#     print(cow)

## 파이어볼 이동
for i in range(K):
    # 이동하고 분리할 때 까지 사용
    board = [[[] for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if len(info[y][x]) != 0:
                for tmp_info in info[y][x]:
                    m, s, d = tmp_info[0], tmp_info[1], tmp_info[2]
                    ny = (y + s * move[d][0]) % N
                    nx = (x + s * move[d][1]) % N
                    board[ny][nx].append([m, s, d])
    # print("이동 후 파이어 볼 합치는 계산 전 board")
    # for cow in board:
    #     print(cow)
    for y in range(N):
        for x in range(N):
            if len(board[y][x]) >= 2:
                total_m, total_s, total_d, cnt, d_4 = 0, 0, [], 0, []
                for info_fireball in board[y][x]:
                    m, s, d = info_fireball[0], info_fireball[1], info_fireball[2]
                    total_m += m
                    total_s += s
                    cnt += 1
                    total_d.append(d % 2)
                m_4 = total_m // 5
                board[y][x] = []
                if m_4 == 0:
                    continue
                s_4 = total_s // cnt
                if len(set(total_d)) == 1:
                    for d in [0, 2, 4, 6]:
                        board[y][x].append([m_4, s_4, d])
                else:
                    for d in [1, 3, 5, 7]:
                        board[y][x].append([m_4, s_4, d])
    info = [tmp_list for tmp_list in board]
    # print("파이어볼 분리 후 원래 info")
    # for cow in info:
    #     print(cow)


result = 0
for y in range(N):
    for x in range(N):
        if info[y][x] != 0:
            for tmp_info in info[y][x]:
                result += tmp_info[0]
print(result)










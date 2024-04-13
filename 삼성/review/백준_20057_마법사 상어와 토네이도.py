# 흩날리는 비율 - 정수 / 나머지 -> a에 들어감
# (1, 1)인 순간 종료 -> (1, 1)일 때 모래 날리기 진행x -> 따로 진행해야 함
# 밖으로 나간 모래 양 구하기

def check(array):
    for cow in array:
        print(cow)
    print()

# 모래 계산 비율(방향에 따른)
move_left = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]
move_up = list(map(list, zip(*move_left[::-1])))
move_right = [tmp[::-1] for tmp in move_left[::-1]]
move_down = [tmp[::-1] for tmp in list(map(list, zip(*move_left[::-1])))[::-1]]

# 나중에 계산해야하는 알파의 위치
alpha = [[2, 1], [3, 2], [2, 3], [1, 2]]

# 방향 (좌, 하, 우, 상)
d = [[0, -1], [1, 0], [0, 1], [-1, 0]]

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# print("초기 모래 그래프 출력")
# for cow in graph:
#     print(cow)

# 토네이도 변수 초기화
cur_y = n // 2
cur_x = n // 2
move_cnt = 0
d_idx = 0
dist = 1
result = 0

while cur_y != 0 or cur_x != 0:
    dy, dx = d[d_idx]
    for _ in range(dist):
        cur_y = cur_y + dy
        cur_x = cur_x + dx
        if cur_y == 0 and cur_x == 0:
            break
        cur_sand = graph[cur_y][cur_x]
        # 현재 좌표를 모래 비율 계산을 위해 좌표 옮기기
        tmp_x = cur_x - 2
        tmp_y = cur_y - 2
        if d_idx == 0:
            notAlphaSand = 0
            graph[cur_y][cur_x] = 0
            for y in range(5):
                for x in range(5):
                    if move_left[y][x] == 0:
                        continue
                    tmp_sand = int(cur_sand * move_left[y][x])
                    if 0 <= y + tmp_y < n and 0 <= x + tmp_x < n:
                        graph[y + tmp_y][x + tmp_x] += tmp_sand
                    else:
                        result += tmp_sand
                    notAlphaSand += tmp_sand
            alpha_y, alpha_x = alpha[d_idx]
            if 0 <= alpha_y + tmp_y < n and 0 <= alpha_x + tmp_x < n:
                graph[alpha_y + tmp_y][alpha_x + tmp_x] += (cur_sand - notAlphaSand)
            else:
                result += (cur_sand - notAlphaSand)
        elif d_idx == 1:
            notAlphaSand = 0
            graph[cur_y][cur_x] = 0
            for y in range(5):
                for x in range(5):
                    if move_down[y][x] == 0:
                        continue
                    tmp_sand = int(cur_sand * move_down[y][x])
                    if 0 <= y + tmp_y < n and 0 <= x + tmp_x < n:
                        graph[y + tmp_y][x + tmp_x] += tmp_sand
                    else:
                        result += tmp_sand
                    notAlphaSand += tmp_sand
            alpha_y, alpha_x = alpha[d_idx]
            if 0 <= alpha_y + tmp_y < n and 0 <= alpha_x + tmp_x < n:
                graph[alpha_y + tmp_y][alpha_x + tmp_x] += (cur_sand - notAlphaSand)
            else:
                result += (cur_sand - notAlphaSand)
        elif d_idx == 2:
            notAlphaSand = 0
            graph[cur_y][cur_x] = 0
            for y in range(5):
                for x in range(5):
                    if move_right[y][x] == 0:
                        continue
                    tmp_sand = int(cur_sand * move_right[y][x])
                    if 0 <= y + tmp_y < n and 0 <= x + tmp_x < n:
                        graph[y + tmp_y][x + tmp_x] += tmp_sand
                    else:
                        result += tmp_sand
                    notAlphaSand += tmp_sand
            alpha_y, alpha_x = alpha[d_idx]
            if 0 <= alpha_y + tmp_y < n and 0 <= alpha_x + tmp_x < n:
                graph[alpha_y + tmp_y][alpha_x + tmp_x] += (cur_sand - notAlphaSand)
            else:
                result += (cur_sand - notAlphaSand)
        elif d_idx == 3:
            notAlphaSand = 0
            graph[cur_y][cur_x] = 0
            for y in range(5):
                for x in range(5):
                    if move_up[y][x] == 0:
                        continue
                    tmp_sand = int(cur_sand * move_up[y][x])
                    if 0 <= y + tmp_y < n and 0 <= x + tmp_x < n:
                        graph[y + tmp_y][x + tmp_x] += tmp_sand
                    else:
                        result += tmp_sand
                    notAlphaSand += tmp_sand
            alpha_y, alpha_x = alpha[d_idx]
            if 0 <= alpha_y + tmp_y < n and 0 <= alpha_x + tmp_x < n:
                graph[alpha_y + tmp_y][alpha_x + tmp_x] += (cur_sand - notAlphaSand)
            else:
                result += (cur_sand - notAlphaSand)
        # print("밖으로 나간 모래")
        # print(result)
        # print("토네이도 이동 후 모래 변화")
        # for cow in graph:
        #     print(cow)
        # print()
    d_idx = (d_idx + 1) % 4
    move_cnt += 1
    if move_cnt == 2:
        move_cnt = 0
        dist += 1

## 0,0 모래 비율 구하기
cur_sand = graph[0][0]
in_sand = int(cur_sand * 0.02) + int(cur_sand * 0.07) + int(cur_sand * 0.01)
out_sand = int(cur_sand * 0.07) + int(cur_sand * 0.01) + int(cur_sand * 0.02) + int(cur_sand * 0.1) * 2 + int(cur_sand * 0.05)
alpha_sand = cur_sand - in_sand - out_sand
result += (out_sand + alpha_sand)
print(result)











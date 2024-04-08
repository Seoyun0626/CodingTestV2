# 비바라기 시전 -> 4칸 정사각형 비구름 생성
# 물복사버그 -> 대각선 방향 거리 1인 칸 물이 있는 바구니 수만큼 증가 + 이때 경계넘어가는 대각선은 고려X
# 이동 명령(방향 + 거리)
d = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

n, m = map(int, input().split())
cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)] # 초기 비구름 상태
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
move = []
for _ in range(m):
    move.append(list(map(int, input().split())))
# print(graph)
# print(move)

for d_idx, dist in move:
    move_cloud = []
    for y, x in cloud:
        ## 구름 이동 + 바구니 물의 양 증가
        ny = (y + d[d_idx][0] * dist) % n
        nx = (x + d[d_idx][1] * dist) % n
        graph[ny][nx] += 1
        ## 구름 사라짐
        move_cloud.append((ny, nx))
    for y, x in move_cloud:
        cnt = 0
        if 0 <= x - 1 and 0 <= y - 1:
            if graph[y - 1][x - 1] != 0:
                cnt += 1
        if 0 <= x - 1 and y + 1 < n:
            if graph[y + 1][x - 1] != 0:
                cnt += 1
        if x + 1 < n and y + 1 < n:
            if graph[y + 1][x + 1] != 0:
                cnt += 1
        if x + 1 < n and 0 <= y - 1:
            if graph[y - 1][x + 1] != 0:
                cnt += 1
        graph[y][x] += cnt

    cloud = []
    for y in range(n):
        for x in range(n):
            if graph[y][x] >= 2 and (y, x) not in move_cloud:
                graph[y][x] -= 2
                cloud.append((y, x))

result = 0
for y in range(n):
    for x in range(n):
        result += graph[y][x]
print(result)
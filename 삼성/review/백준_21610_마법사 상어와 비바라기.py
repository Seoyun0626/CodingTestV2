# 비바라기 -> 비구름 생성
# 1번 행 + N번 행 연결 / 1번 열 + N번 열 연결
# 비구름 (N, 1), (N, 2), (N - 1, 1), (N - 1, 2) + M번 이동 명령
# 이동 명령
# 1. 구름 이동
# 2. 물의 양 1증가
# 3. 구름 사라짐
# 4. 증가한 칸 기준 -> 대각선 방향으로 1인 칸 물 바구니 수 만큼 더해짐
# 5. 물의 양 2이상인 칸에 구름(3에서 구름이 사라진 칸이 아니어야 함 -> 중복 금지) + 물의 양 2만큼 줄어듬
## 물의 양 합


n, m = map(int, input().split())
graph = []
info = []
cloud = [n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]
move = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
check_move = [[-1, -1], [-1, 1], [1, -1], [1, 1]]

for _ in range(n):
    graph.append(list(map(int, input().split())))
for _ in range(m):
    info.append(list(map(int, input().split())))

for d_idx, dist in info:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    dy, dx = move[d_idx]
    ## 구름 이동
    # print("구름 이동 후 좌표")
    move_cloud = []
    for y, x in cloud:
        ny = (y + dist * dy) % n
        nx = (x + dist * dx) % n
        move_cloud.append((ny, nx))
        graph[ny][nx] += 1
        visited[ny][nx] = 1
    ## 대각선 방향 물 증가
    for y, x in move_cloud:
        iswater = 0
        for dy, dx in check_move:
            if 0 <= y + dy < n and 0 <= x + dx < n:
                if graph[y + dy][x + dx] != 0:
                    iswater += 1
        graph[y][x] += iswater
    # print("대각선 물의 양 증가 한 후 graph")
    # for cow in graph:
    #     print(cow)
    #
    # print("새롭게 생성된 구름 좌표")
    ## 구름 생성
    cloud = []
    for y in range(n):
        for x in range(n):
            if graph[y][x] >= 2 and visited[y][x] == 0:
                cloud.append((y, x))
                graph[y][x] -= 2
    # print(new_cloud)
    # print("구름 생성으로 인한 graph 물의 양 감소")
    # for cow in graph:
    #     print(cow)

result = 0
for cow in graph:
    result += sum(cow)
print(result)




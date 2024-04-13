# q번 동안
# 격자 나누기 -> 90도 회전
# 3개 미만인 경우 -> 얼음 양 1 줄어듬

## 남아 있는 얼음 합 + 큰 덩어리 칸의 개수

from collections import deque

n, q = map(int, input().split())
map_size = 2 ** n
move = [[0, -1], [1, 0], [0, 1], [-1, 0]]
graph = []
level = []
for _ in range(map_size):
    graph.append(list(map(int, input().split())))
level.extend(map(int, input().split()))

# print("초기 그래프 출력")
# # for cow in graph:
# #     print(cow)
# # print("레벨 출력")
# # print(level)

def rotate(graph, small_size):
    new_graph = [[0 for _ in range(map_size)]for _ in range(map_size)]
    for i in range(0, map_size, small_size):
        for j in range(0, map_size, small_size):
            for k in range(small_size):
                for m in range(small_size):
                    new_graph[i + k][j + m] = graph[i + (small_size - 1) - m][j + k]
    return new_graph

def check_ice(graph):
    new_graph = [[0 for _ in range(map_size)]for _ in range(map_size)]
    for y in range(len(graph)):
        for x in range(len(graph)):
            if graph[y][x] == 0:
                new_graph[y][x] = graph[y][x]
                continue
            ice_cnt = 0
            for dy, dx in move:
                if 0 <= y + dy < map_size and  0 <= x + dx < map_size:
                    if graph[y + dy][x + dx] != 0:
                        ice_cnt += 1
            if ice_cnt < 3:
                new_graph[y][x] = graph[y][x] - 1
            else:
                new_graph[y][x] = graph[y][x]
    return new_graph

for i in range(q):
    small_size = (2 ** level[i])
    graph = rotate(graph, small_size)
    # print("회전 후 그래프")
    # for cow in graph:
    #     print(cow)
    graph = check_ice(graph)
    # print("얼음 체크 후 그래프")
    # for cow in graph:
    #     print(cow)


sum_ice = 0
max_size = 0
cur_size = 0
visited = [[0 for _ in range(map_size)] for _ in range(map_size)]

for y in range(len(graph)):
    for x in range(len(graph)):
        if graph[y][x] > 0 and visited[y][x] == 0:
            sum_ice += graph[y][x]
            visited[y][x] = 1
            queue = deque()
            queue.append((y, x))
            cur_size = 1

            while queue:
                ny, nx = queue.popleft()
                for dy, dx in move:
                    if 0 <= ny + dy < map_size and 0 <= nx + dx < map_size:
                        if graph[ny + dy][nx + dx] > 0 and visited[ny + dy][nx + dx] == 0:
                            cur_size += 1
                            sum_ice += graph[ny + dy][nx + dx]
                            visited[ny + dy][nx + dx] = 1
                            queue.append((ny + dy, nx + dx))
        max_size = max(max_size, cur_size)
print(sum_ice)
print(max_size)


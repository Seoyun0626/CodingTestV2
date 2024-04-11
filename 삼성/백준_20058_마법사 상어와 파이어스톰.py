# L단계 결정 -> 시계 방향 90도 회전 -> 얼음이 있는 칸(3개이상) 인접하지 않은 칸은 얼음 양 1감소

from collections import deque

# 파이어 스톰 시전
n, q = map(int, input().split())
map_size = 2 ** n
graph = []
move = [[0, -1], [1, 0], [0, 1], [-1, 0]]
queue = deque()

for _ in range(map_size):
    graph.append(list(map(int, input().split())))
level = list(map(int, input().split()))

# print("그래프 출력")
# for cow in graph:
#     print(cow)
#
# print("level 출력")
# print(level)

def rotate_90(small_graph_size, graph):
    new_graph = [[] for _ in range(map_size)]
    for i in range(0, map_size, small_graph_size):
        for j in range(0, map_size, small_graph_size):
            tmp = []
            for k in range(small_graph_size):
                tmp.append(graph[i + k][j : j + small_graph_size])
            tmp = list(map(list, zip(*tmp[::-1])))
            for l in range(small_graph_size):
                new_graph[i + l].extend(tmp[l])
    # for cow in new_graph:
    #     print(cow)
    return new_graph

def minus(graph):
    new_graph = [[0 for _ in range(map_size)] for _ in range(map_size)]

    for y in range(map_size):
        for x in range(map_size):
            cnt = 0
            for dy, dx in move:
                if 0 <= y + dy < map_size and 0 <= x + dx < map_size:
                    if graph[y + dy][x + dx] != 0:
                        cnt += 1
            if graph[y][x] != 0 and cnt < 3:
                new_graph[y][x] = graph[y][x] - 1
            else:
                new_graph[y][x] = graph[y][x]

    return new_graph




for i in range(q):
    # print("파이어스톰 시전")
    small_graph_size = 2 ** (level[i])
    graph = rotate_90(small_graph_size, graph)
    # print("90도 회전 후 그래프")
    # for cow in graph:
    #     print(cow)
    # print()
    graph = minus(graph)
    # print("minus함수 후 그래프")
    # for cow in graph:
    #     print(cow)

## 덩어리 구하는 함수
sum_ice = 0
max_size = 0
visited = [[0 for _ in range(map_size)] for _ in range(map_size)]
now_size = 1

for y in range(map_size):
    for x in range(map_size):
        if graph[y][x] > 0 and visited[y][x] == 0:
            queue.append((y, x))
            sum_ice += graph[y][x]
            visited[y][x] = 1
            now_size = 1

            while queue:
                ny, nx = queue.popleft()
                for dy, dx in move:
                    nny = ny + dy
                    nnx = nx + dx
                    if 0 <= nny < map_size and 0 <= nnx < map_size:
                        if graph[nny][nnx] > 0 and visited[nny][nnx] == 0:
                            sum_ice += graph[nny][nnx]
                            visited[nny][nnx] = 1
                            now_size += 1
                            queue.append((nny, nnx))

        max_size = max(max_size, now_size)

print(sum_ice)
print(max_size)






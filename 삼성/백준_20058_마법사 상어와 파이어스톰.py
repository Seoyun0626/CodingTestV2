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
level= list(map(int, input().split()))

# print("그래프 출력")
# for cow in graph:
#     print(cow)
#
# print("level 출력")
# print(level)

def rotate_90(small_graph_size):
    global graph
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
    graph = new_graph
    return graph

def minus(rotate_graph, y, x):
    cnt = 0
    for dy, dx in move:
        if 0 <= y + dy < map_size and 0 <= x + dx < map_size:
            if rotate_graph[y + dy][x + dx] != 0:
                cnt += 1
    if cnt < 3:
        minus_list.append((y, x))




for i in range(q):
    print("파이어스톰 시전")
    small_graph_size = 2 ** (level[i])
    rotate_graph = rotate_90(small_graph_size)
    # print("90도 회전 후 그래프")
    # for cow in rotate_graph:
    #     print(cow)
    minus_list = []
    for y in range(len(rotate_graph)):
        for x in range(len(rotate_graph)):
            if rotate_graph[y][x] != 0:
                minus(rotate_graph, y, x)
    for y, x in minus_list:
        rotate_graph[y][x] -= 1
    print("minus함수 후 그래프")
    for cow in rotate_graph:
        print(cow)

def bigIce(y, x, visited, cnt):

    visited[y][x] = cnt
    maxbigIce = 0

    for dy, dx in move:
        if 0 <= y + dy < map_size and 0 <= x + dx < map_size:
            if rotate_graph[y + dy][x + dx] != 0 and visited[y + dy][x + dx] == 0:
                bigIce(y + dy, x + dx, visited, cnt + 1)
    print("y, x에서 visited")
    for cow in visited:
        print(cow)
    for cow in visited:
        if max(cow) > maxbigIce:
            maxbigIce = max(cow)
    return maxbigIce


## 남아 있는 얼음 합
result1 = 0
for cow in rotate_graph:
    result1 += sum(cow)
print(result1)

## 가장 큰 덩어리 칸의 개수
result2 = 0
for y in range(len(rotate_graph)):
    for x in range(len(rotate_graph)):
        if rotate_graph[y][x] != 0:
            visited = [[0 for _ in range(len(rotate_graph))] for _ in range(len(rotate_graph))]
            tmp_cnt = bigIce(y, x, visited, 1)
            if result2 < tmp_cnt:
                result2 = tmp_cnt
print(result2)



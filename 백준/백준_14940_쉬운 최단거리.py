from collections import deque

import sys
input = sys.stdin.readline

# 0 : 갈 수 없음, 1 : 갈 수 있음, 2 : 목표 지점
n, m = map(int, input().split())
graph = []
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
result = [[-1 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))
# print(graph)
# print(result)

for y in range(n):
    for x in range(m):
        if graph[y][x] == 2:
            cur_y, cur_x = y, x

result[cur_y][cur_x] = 0
visited[cur_y][cur_x] = 1
queue = deque()
queue.append((cur_y, cur_x))

while queue:
    cur_y, cur_x = queue.popleft()
    # print(cur_y, cur_x, queue)
    for dy, dx in move:
        if 0 <= cur_y + dy < n and 0 <= cur_x + dx < m:
            if graph[cur_y + dy][cur_x + dx] == 0 and visited[cur_y + dy][cur_x + dx] == 0:
                result[cur_y + dy][cur_x + dx] = 0
                visited[cur_y + dy][cur_x + dx] = 1
            elif graph[cur_y + dy][cur_x + dx] == 1 and visited[cur_y + dy][cur_x + dx] == 0:
                visited[cur_y + dy][cur_x + dx] = 1
                result[cur_y + dy][cur_x + dx] = result[cur_y][cur_x] + 1
                queue.append((cur_y + dy, cur_x + dx))

for y in range(n):
    for x in range(m):
        if graph[y][x] == 0 and result[y][x] == -1:
            result[y][x] = 0

for cow in result:
    print(*cow)


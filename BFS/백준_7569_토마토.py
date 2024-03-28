from collections import deque

# x, y, z = m, n, h
# z, y, x
move = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, 1], [0, 0, -1]]

m, n, h = map(int, input().split()) # 가로, 세로, 높이
graph = []

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
    graph.append(tmp)
# print(graph)

queue = deque()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 1:
                queue.append((x, y, z))
# print(queue)
def bfs():
    while queue:
        x, y, z = queue.popleft()

        for dz, dy, dx in move:
            if 0 <= z+dz < h and 0 <= y+dy < n and 0 <= x+dx < m:
                if graph[z+dz][y+dy][x+dx] == 0:
                    graph[z+dz][y+dy][x+dx] = graph[z][y][x] + 1
                    queue.append((x+dx, y+dy, z+dz))
bfs()

day = 0

for height in graph:
    for cow in height:
        for tomato in cow:
            if tomato == 0:
                print(-1)
                exit()
            else:
                day = max(day, tomato)
print(day - 1)


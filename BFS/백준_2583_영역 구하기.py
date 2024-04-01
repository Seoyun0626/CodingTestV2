from collections import deque

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
m, n, k = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(m)]
result = []
cnt = 0
# for cow in graph:
#     print(cow)


for _ in range(k):
    left_x, left_y, right_x, right_y = map(int, input().split())
    for y in range(left_y, right_y):
        for x in range(left_x, right_x):
            graph[y][x] = 1
# for cow in graph:
#     print(cow)

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    size = 1
    while queue:
        x, y = queue.popleft()
        # print(x, y)
        for dy, dx in move:
            if 0 <= x + dx < n and 0 <= y + dy < m:
                if graph[y + dy][x + dx] == 0:
                    queue.append((x + dx, y + dy))
                    graph[y + dy][x + dx] = 1
                    size += 1
    result.append(size)

for y in range(m):
    for x in range(n):
        if graph[y][x] == 0:
            graph[y][x] = 1
            cnt += 1
            # print("enter bfs", x, y)
            bfs(x, y)
result.sort()
print(cnt)
print(*result)


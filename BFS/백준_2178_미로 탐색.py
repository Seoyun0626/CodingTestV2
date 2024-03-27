from collections import deque

n, m = map(int, input().split())
move = [[1, 0], [-1, 0], [0, 1], [0, -1]] # 하,상,우,좌
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
# print(graph)

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # print("queue", queue, "x:",x, "y:", y)
        for dy , dx in move:
            if 0 <= x+dx < m and 0 <= y+dy < n:
                if graph[y+dy][x+dx] == 1:
                    queue.append((x+dx, y+dy))
                    graph[y+dy][x+dx] = graph[y][x] + 1
bfs(0,0)
print(graph[n-1][m-1])


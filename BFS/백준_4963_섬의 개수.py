from collections import deque

move = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()
        for dy, dx in move:
            if 0 <= x+dx < w and 0 <= y+dy < h:
                if graph[y+dy][x+dx] == 1 and visited[y+dy][x+dx] == False:
                    queue.append((x+dx, y+dy))
                    visited[y+dy][x+dx] = True

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    visited = [[False for i in range(w)] for j in range(h)]
    cnt = 0
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    # print(graph)
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1 and visited[y][x] == False:
                # print(x, y, visited)
                cnt += 1
                bfs(x, y)
    print(cnt)

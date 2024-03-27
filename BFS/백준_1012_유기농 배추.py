from collections import deque
move = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상,하,좌,우
t = int(input())

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()
        for dy, dx, in move:
            if 0 <= x+dx < m and 0 <= y+dy <n:
                if graph[y+dy][x+dx] == 1 and visited[y+dy][x+dx] == False:
                    visited[y+dy][x+dx] = True
                    queue.append((x+dx, y+dy))

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for j in range(m)] for i in range(n)]
    visited = [[False for j in range(m)] for i in range(n)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    # print(graph)
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1 and visited[y][x] == False:
                cnt += 1
                bfs(x, y, visited)
    print(cnt)




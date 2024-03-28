from collections import deque

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
n = int(input())
graph = []
result = []
visited = [[False for i in range(n)] for j in range(n)]
cnt = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))
# print(graph)

max_height = max(map(max, graph))
# print(max_height)

def bfs(x, y, height):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()
        # print(x, y)
        for dy, dx in move:
            if 0 <= x+dx < n and 0 <= y+dy < n:
                if graph[y+dy][x+dx] > height and visited[y+dy][x+dx] == False:
                    queue.append((x+dx, y+dy))
                    visited[y+dy][x+dx] = True
    # print("end")


for height in range(0, max_height+1):
    # print("height", height)
    visited = [[False for i in range(n)] for j in range(n)]
    cnt = 0
    for y in range(n):
        for x in range(n):
            if graph[y][x] > height and visited[y][x] == False:
                # print("Start", x, y, graph[y][x], height)
                cnt += 1
                bfs(x, y, height)
    result.append(cnt)
print(max(result))



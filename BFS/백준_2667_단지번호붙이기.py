from collections import deque

n = int(input())
move = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상,하,좌,우
visited = [[False for i in range(n)] for j in range(n)]
graph = []
result = []
town = 0

for _ in range(n):
    graph.append(list(map(int, input())))
# print(graph)

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    home = 1

    while queue:
        x, y = queue.popleft()
        # print(x, y, home)
        for dy, dx in move:
            if 0 <= x+dx < n and 0 <= y+dy < n:
                if graph[y+dy][x+dx] == 1 and visited[y+dy][x+dx] == False:
                    home += 1
                    visited[y+dy][x+dx] = True
                    queue.append((x+dx, y+dy))
    return home

for y in range(n):
    for x in range(n):
        if graph[y][x] == 1 and visited[y][x] == False:
            # print("x", x, "y", y)
            home_cnt = bfs(x, y)
            result.append(home_cnt)
            town += 1
# print(dict)
print(town)
result.sort()
for home in result:
    print(home)




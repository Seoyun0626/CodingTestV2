import sys
sys.setrecursionlimit(10**5)

t = int(input())
## 동남서북 방향 설정
move = [[0,1], [1,0], [0,-1],[-1,0]]

def dfs(graph, x, y, visited):

    if 0 > x or x >= m or 0 > y or y >= n or graph[y][x] == 0 or visited[y][x] == True:
        return

    visited[y][x] = True

    for dx, dy in move:
        dfs(graph, x+dx, y+dy, visited)

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for i in range(m)] for j in range(n)]
    visited = [[False for i in range(m)] for j in range(n)]
    result = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for x in range(m):
        for y in range(n):
            if graph[y][x] == 1 and visited[y][x] == False:
                result += 1
                # print(x, y)
                dfs(graph, x, y, visited)
    print(result)


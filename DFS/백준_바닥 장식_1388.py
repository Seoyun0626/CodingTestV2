## DFS 구현
def dfs(x, y):
    if graph[y][x] == "|":
        visited[y][x] = True
        dx = x
        dy = y + 1
        if 0 <= dy < n and graph[dy][dx] == "|" and visited[dy][dx] == False:
            dfs(dx, dy)
        else:
            return
    elif graph[y][x] == "-":
        visited[y][x] = True
        dx = x + 1
        dy = y
        if 0 <= dx < m and graph[dy][dx] == "-" and visited[dy][dx] == False:
            dfs(dx, dy)
        else:
            return

## 변수 설정
n, m = map(int, input().split()) # 세로, 가로
graph = []
visited = [[False for i in range(m)] for j in range(n)]
cnt = 0
# print(visited)

## 그래프 그리기
for i in range(n):
    tmp = list(input())
    graph.append(tmp)
# print(graph)

## 개수 세기
for y in range(n):
    for x in range(m):
        if visited[y][x] == False:
            dfs(x, y)
            cnt += 1
print(cnt)



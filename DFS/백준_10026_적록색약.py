import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = []
answer1 = 0
answer2 = 0
visited = [[False for i in range(n)] for j in range(n)]
result = []

move = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 우, 하, 좌, 상

for _ in range(n):
    tmp = list(map(str, input()))
    graph.append(tmp)
# print(graph)

def dfs(x, y, color, visited):

    visited[y][x] = True

    for dy, dx in move:
        if (0 <= x+dx < n) and (0 <= y+dy < n):
            if visited[y+dy][x+dx] == False and graph[y+dy][x+dx] == color:
                dfs(x+dx, y+dy, color, visited)

for i in range(n):
    for j in range(n):
        color = graph[i][j]
        if visited[i][j] == False:
            answer1 += 1
            dfs(j, i, color, visited)
            # print(j, i, color, visited1)
# print(answer1)

for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"

visited = [[False for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        color = graph[i][j]
        if visited[i][j] == False:
            answer2 += 1
            # print("start", j, i, color, visited2)
            dfs(j, i, color, visited)
            # print("result", j, i, color, visited2)
# print(answer2)

print(answer1, answer2)

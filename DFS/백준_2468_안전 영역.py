import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = []
result = []
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(n):
    graph.append(list(map(int, input().split())))
# print(graph)
max_height = max(map(max, graph))
min_height = min(map(min, graph))
# print(max_height)
height = min_height - 1

def dfs(x, y, height, visited):
    visited[y][x] = True

    for dy, dx in move:
        if (0 <= x+dx < n) and (0 <= y+dy < n):
            if (visited[y+dy][x+dx] == False) and (graph[y+dy][x+dx] > height):
                dfs(x+dx, y+dy, height, visited)



while height < (max_height):
    visited = [[False for i in range(n)] for j in range(n)]
    answer = 0
    for y in range(n):
        for x in range(n):
            if visited[y][x] == False and graph[y][x] > height:
                answer += 1
                dfs(x, y, height, visited)
    height += 1
    result.append(answer)
# print(result)
print(max(result))

import sys
sys.setrecursionlimit(10 ** 6)

r, c = map(int, input().split()) #세로, 가로
graph = []
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[False for i in range(c)] for j in range(r)]
color = []

for _ in range(r):
    graph.append(list(input()))
# print(graph)

color.append(graph[0][0])

def dfs(x, y, visited, color):
    visited[y][x] = True

    # print(x, y, visited, color_list)

    for dy, dx in move:
        if (0 <= x+dx < c) and (0 <= y+dy < r):
            if graph[y+dy][x+dx] not in color:
                color.append(graph[y+dy][x+dx])
                print(x + dx, y + dy, color, visited)
                dfs(x+dx, y+dy, visited, color)

print(0, 0, color, visited)
dfs(0, 0, visited, color)
# print(len(color))
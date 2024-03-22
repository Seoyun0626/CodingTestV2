move = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]] # 우하좌상

import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):

    # 재귀 종료 조건
    if x < 0 or x >= w or y < 0 or y >= h or visited[y][x] == True or graph[y][x] == 0:
        return
    visited[y][x] = True
    # print(x, y)

    for tmp in move:
        dy = tmp[0]
        dx = tmp[1]
        dfs(x+dx, y+dy)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    cnt = 0
    visited = [[False for i in range(w)] for j in range(h)]
    for _ in range(h):
        tmp = list(map(int, input().split()))
        graph.append(tmp)
    # print(graph)
    for i in range(h):
        for j in range(w):
            if visited[i][j] == False and graph[i][j] == 1:
                cnt += 1
                dfs(j, i)
    print(cnt)
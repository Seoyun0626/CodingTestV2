from collections import deque
import sys
input = sys.stdin.readline

move = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상,하,좌,우
m, n = map(int, input().split())
day = 0
flag = 0
graph = []
visited = [[False for i in range(m)] for j in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))
# print(graph)


# 저장될 때부터 모든 토마토가 익은 경우(0)
tmp = []
for y in range(n):
    for x in range(m):
        tmp.append(graph[y][x])
if 0 not in tmp:
    flag = 1

# 모든 토마토가 익을 수 없는 경우:
for y in range(n):
    for x in range(m):
        result = []
        if graph[y][x] == 0:
            for dy, dx in move:
                if 0 <= x+dx < m and 0 <= y+dy < n:
                    result.append(graph[y+dy][x+dx])
            result = set(result)
            if len(result) == 1 and -1 in result:
                flag = 2
                break

def bfs(tomato_list, visited):
    for x, y in tomato_list:
        queue = deque()
        queue.append((x, y))
        visited[y][x] = True

        x, y = queue.popleft()
        # print(x, y)
        for dy, dx in move:
            if 0 <= x+dx < m and 0 <= y+dy < n:
                # print(x+dx, y+dy)
                if visited[y+dy][x+dx] == False and graph[y+dy][x+dx] != -1:
                    graph[y+dy][x+dx] = 1
    # print("End", visited, graph)


if flag == 0:
    # 무조건 토마토가 다 익을 수 있는 경우
    while True:
        tomato_list = []
        for y in range(n):
            for x in range(m):
                if graph[y][x] == 1 and visited[y][x] == False:
                    tomato_list.append((x, y))
        # print("Start", tomato_list, visited)
        bfs(tomato_list, visited)
        day += 1

        tmp = []
        for y in range(n):
            for x in range(m):
                tmp.append(graph[y][x])
        if 0 not in tmp:
            break

if flag == 0:
    print(day)
elif flag == 1:
    print(0)
else:
    print(-1)



import copy
from collections import deque

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
n, m = map(int, input().split())
visited = [[False for i in range(m)] for j in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# print(graph)



def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)

    for y in range(n):
        for x in range(m):
            if graph[y][x] == 2:
                queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for dy, dx in move:
            if 0 <= x+dx < m and 0 <= y+dy < n:
                if tmp_graph[y+dy][x+dx] == 0:
                    queue.append((x+dx, y+dy))
                    tmp_graph[y+dy][x+dx] = 2
    global answer
    zeroCnt = 0
    for cow in tmp_graph:
        zeroCnt += cow.count(0)
    answer = max(answer, zeroCnt)

def makeWall(cnt):

    # 벽 3개를 세우면 바이러스 퍼뜨리기
    if cnt == 3:
        bfs()
        return

    for y in range(n):
        for x in range(m):
            if graph[y][x] == 0:
                # 벽 세우기
                graph[y][x] = 1
                makeWall(cnt+1)
                # 최적해가 아니면 벽 세운거 허물기
                graph[y][x] = 0

answer = 0
makeWall(0)
print(answer)







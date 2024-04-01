import copy
import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

def bfs(graph):
    queue = deque([(j, i) for i in range(n) for j in range(m) if graph[i][j] == 2])

    while queue:
        x, y = queue.popleft()
        for dy, dx in move:
            if (0 <= x+dx < m) and (0 <= y+dy < n) and (graph[y+dy][x+dx] == 0):
                queue.append((x+dx, y+dy))
                graph[y+dy][x+dx] = 2
    global answer
    zeroCnt = 0
    for cow in graph:
        zeroCnt += cow.count(0)
    answer = max(answer, zeroCnt)
    # print(answer, zeroCnt)

input = sys.stdin.readline
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
x_y = [(x, y) for x in range(m) for y in range(n) if graph[y][x] == 0]
answer = 0

# 벽 세울 수 있는 조합 구성
for c in combinations(x_y, 3):
    tmp_graph = deepcopy(graph)
    for x, y in c:
        tmp_graph[y][x] = 1
    bfs(tmp_graph)
print(answer)
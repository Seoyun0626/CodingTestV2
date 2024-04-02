from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
result = []
answer = 0
for _ in range(m):
    a, b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# for cow in graph:
#     print(cow)
# print(visited)

def bfs(i):
    queue = deque()
    queue.append(i)
    visited = [0] * (n + 1)
    visited[i] = 1
    while queue:
        node = queue.popleft()
        # print(visited)
        for v in graph[node]:
            if visited[v] == 0:
                visited[v] = visited[node] + 1
                queue.append(v)
    # print("final", visited)

    result.append(sum(visited)-n)


for i in range(1, n + 1):
    # print("start bfs", i)
    bfs(i)
# print(result)
answer_cnt = min(result)

for i in range(len(result)):
    num = result[i]
    if num == answer_cnt:
        print(i+1)
        break


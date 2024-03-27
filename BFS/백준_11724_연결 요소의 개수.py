from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# print(graph)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if visited[node] == False:
                queue.append(node)
                visited[node] = True

for i in range(1, n+1):
    if visited[i] == False:
        cnt += 1
        bfs(i)
print(cnt)
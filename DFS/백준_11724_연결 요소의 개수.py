import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
cnt = 0
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# print(graph, visited)

def dfs(v):

    if visited[v] == True:
        return
    visited[v] = True

    for v in graph[v]:
        dfs(v)

for i in range(1, n+1):
    if visited[i] == False:
        cnt += 1
        dfs(i)
print(cnt)


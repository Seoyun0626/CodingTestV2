from collections import deque

n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph, visited)

for i in graph:
    i.sort()
# print(graph, visited)


def dfs(v, visited):
    visited[v] = True

    print(v, end=" ")

    for node in graph[v]:
        if visited[node] == False:
            dfs(node, visited)
dfs(v, visited)

visited = [False] * (n+1)

print()

def bfs(v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
bfs(v, visited)

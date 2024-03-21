n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

def dfs(graph, v, visited):

    if visited[v] == True:
        return
    visited[v] = True

    for tmp in graph[v]:
        dfs(graph, tmp, visited)
    # print(visited)

dfs(graph, 1, visited)

result = visited.count(True) - 1
print(result)
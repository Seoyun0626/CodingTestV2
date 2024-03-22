import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())

graph = [[] for i in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

def dfs(v):

    for node in graph[v]:
        if visited[node] == False:
            visited[node] = v
            # print(visited)
            dfs(node)


visited = [False] * (n + 1)
dfs(1)

for i in range(2, n+1):
    print(visited[i])
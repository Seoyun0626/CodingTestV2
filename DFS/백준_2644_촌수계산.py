n = int(input())
a, b = map(int, input().split())

graph = [[] for i in range(n+1)]
m = int(input())
visited = [False] * (n+1)
result = []
for _ in range(m):
    x, y = map(int, input().split()) # x : 부모 y : 자식
    graph[x].append(y)
    graph[y].append(x)
# print(graph)
# print(visited)

def dfs(v, cnt):

    cnt += 1
    visited[v] = True

    if v == b:
        result.append(cnt)

    for tmp in graph[v]:
        if not visited[tmp]:
            # print(tmp, cnt)
            dfs(tmp, cnt)

dfs(a, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)

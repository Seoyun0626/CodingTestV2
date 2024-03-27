from collections import deque

n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

def bfs(v):
    queue = deque()
    queue.append(v)
    answer = 0
    visited[v] = True

    while queue:
        # print(queue)
        tmp = queue.popleft()
        for node in graph[tmp]:
            if visited[node] == False:
                queue.append(node)
                answer += 1
                visited[node] = True
    print(answer)
bfs(1)


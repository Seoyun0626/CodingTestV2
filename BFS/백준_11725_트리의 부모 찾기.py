from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

graph = [[] for i in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
parent = [0] * (n + 1)
queue = deque([1])

def bfs(v):


    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if parent[node] == 0:
                queue.append(node)
                parent[node] = v

bfs(1)

for i in range(2, len(parent)):
    print(parent[i])




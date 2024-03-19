# DFS

def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)

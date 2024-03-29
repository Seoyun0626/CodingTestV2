from collections import deque

# BFS
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])

    # 현재 노드 방문 처리
    visited[start] = True

    # 큐가 빌 때 까지 반복
    while queue:
        # 큐에서 하나의 원소 뽑아 출력
        v = queue.popleft()
        print(v, end=" ")

        # 해당 원소와 연결된, 아직 방문하지 않은 원소 큐 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

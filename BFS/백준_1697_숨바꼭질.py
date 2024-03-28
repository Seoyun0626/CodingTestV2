from collections import deque

# 각각의 위치(n, k)를 좌표처럼 생각하기 + 최단 시간 => bfs
n, k = map(int, input().split())
MAX = 100001
graph = [0] * MAX


def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        v = queue.popleft()

        # print(v)
        if v == k:
            print(graph[v])
            break
        for cur in (v-1, v+1, v*2):
           if 0 <= cur < MAX and graph[cur] == 0:
                queue.append(cur)
                graph[cur] = graph[v] + 1
        # print(queue)

bfs()



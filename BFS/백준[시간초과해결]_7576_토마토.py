# point1 : bfs 돌린 후 예외/정상 처리 방식으로 접근

from collections import deque

move = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상, 하, 좌, 우
m, n = map(int, input().split())
graph = []
queue = deque()

for _ in range(n):
    graph.append(list(map(int, input().split())))

# point2 : 초기 토마토 익은 위치  queue에 넣기
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            queue.append((x, y))

# BFS 함수 정의
def bfs():
    while queue:
        x, y = queue.popleft()

        for dy, dx in move:
            if 0 <= x+dx < m and 0 <= y+dy < n and graph[y+dy][x+dx] == 0:
                graph[y+dy][x+dx] = graph[y][x] + 1
                queue.append((x+dx, y+dy))
bfs()

# 예외 처리
# tomato가 가질 수 있는 숫자 = [-1, 0, 1이상의 숫자]
# point3 : 바로 종료 시켜야 함 -> exit 함수 사용
day = 0
for row in graph:
    for tomato in row:
        # bfs 결과 0이 존재 하는 경우 -> 익을 수 없음
        if tomato == 0:
            print(-1)
            # 무조건 끝내야 하므로 exit()함수 사용
            exit()
        else:
            day = max(day, tomato)
print(day-1)

# m마리 물고기, 1마리 아기상어
# 아기상어 크기(2)
# 아기상어 크기 < 물고기 크기 : 못 지나감 + 먹을 수 없음
# 아기상어 크기 > 물고기 크기 : 지나감 + 먹을 수 있음
# 아기상어 크기 == 물고기 크기 : 지나감 + 먹을 수 있음
# 먹을 수 있는 물고기 1마리 -> 먹으러 감
# 먹을 수 있는 물고기 2마리 이상 -> 가까운 물고기 먹으러 감 -> 가까운 물고기가 많은 경우 -> 가장 위 물고기 -> 가장 왼쪽 물고기
# 자신의 크기 == 같은 수 물고기 먹으면 -> 크기 1 증가
## 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간

from collections import deque

### 변수 초기화
n = int(input())
time = 0
cur_size = 2
cur_eat = 0
move = [[0, -1], [1, 0], [0, 1], [-1, 0]]
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

### 초기 상어 위치
for y in range(n):
    for x in range(n):
        if graph[y][x] == 9:
            graph[y][x] = 0
            cur_y, cur_x = y, x
            break

def checkFishCnt(graph, fish, cur_y, cur_x):
    global cur_size, cur_eat
    visited = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    queue = deque()
    queue.append((cur_y, cur_x))
    visited[cur_y][cur_x] = 1

    while queue:
        y, x = queue.popleft()
        for dy, dx in move:
            if 0 <= y + dy < n and 0 <= x + dx < n:
                if visited[y + dy][x + dx] == 0:
                    if graph[y + dy][x + dx] == 0:
                        visited[y + dy][x + dx] = visited[y][x] + 1
                        queue.append((y + dy, x + dx))
                        continue
                    if graph[y + dy][x + dx] > cur_size:
                        continue
                    elif graph[y + dy][x + dx] == cur_size:
                        queue.append((y + dy, x + dx))
                        visited[y + dy][x + dx] = visited[y][x] + 1
                    elif graph[y + dy][x + dx] < cur_size:
                        queue.append((y + dy, x + dx))
                        visited[y + dy][x + dx] = visited[y][x] + 1
                        fish.append((y + dy, x + dx, visited[y + dy][x + dx] - 1))

    if len(fish) == 0:
        return []
    else:
        fish = sorted(fish, key = lambda x : (x[2], x[0], x[1]))
        return fish[0]


while True:
    fish = []
    fish = checkFishCnt(graph, fish, cur_y, cur_x)
    if len(fish) == 0:
        break
    ## 먹을 수 있는 물고기가 있는 경우 -> 먹고 + 현재 좌표 바꾸기
    cur_y, cur_x, dist = fish[0], fish[1], fish[2]
    graph[cur_y][cur_x] = 0
    cur_eat += 1
    time += dist
    if cur_eat == cur_size:
        cur_eat = 0
        cur_size += 1
print(time)

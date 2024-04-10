# n * n 크기 / m마리 물고기 / 1마리 상어
# 상어(초기2) / 물고기 => 자연수 크기 가짐
# 아기 상어 < 물고기 => 지나갈 수 없음 + 먹을 수 없음
# 아기 상어 > 물고기 => 지나갈 수 있음 + 먹을 수 있음
# 아기 상어 == 물고기 => 지나갈 수 있음 + 먹을 수 없음

# 먹을 수 있는 물고기 == 1마리 -> 먹으러 가기
# 먹을 수 있는 물고기 > 1마리 -> 가까운 물고기
# 가까운 물고기 많은 경우 -> 가장 위 -> 가장 왼쪽

# 자신의 크기 = 같은 수 물고기 -> 크기 1 증가 ===> 물고기 먹을때마다 비교하기

## 큐 사용(거리 최솟값 구하기 위해)
from collections import deque

## 입력 받기
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

## 좌, 하, 우, 상
move = [[0, -1], [1, 0], [0, 1], [-1, 0]]
## 시간 초기화
time = 0
## 큐
queue = deque()

## 초기 상어 위치
for y in range(n):
    for x in range(n):
        if graph[y][x] == 9:
            graph[y][x] = 0
            cur_y, cur_x = y, x

## 초기 상어 크기
cur_size = 2
cur_eat = 0

## 먹을 수 있는 물고기 있는지 확인함수
fish_index = []
def eatFlag():
    global graph, fish_index, cur_size
    fish_index = []
    for y in range(n):
        for x in range(n):
            if 0 < graph[y][x] < cur_size:
                fish_index.append((y, x))
    if len(fish_index) == 0:
        return False
    else:
        return True

def eatOne():
    fishOne = []
    global time, cur_size, cur_eat, graph, cur_y, cur_x
    visited = [[0 for _ in range(n)] for _ in range(n)]
    queue.append((cur_y, cur_x))
    visited[cur_y][cur_x] = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in move:
            if 0 <= y + dy < n and 0 <= x + dx < n:
                # 방문하지 않는 경우
                if visited[y + dy][x + dx] == 0:
                    ## 물고기 없음
                    if graph[y + dy][x + dx] == 0:
                        visited[y + dy][x + dx] = visited[y][x] + 1
                        queue.append((y + dy, x + dx))
                    ## 목표 물고기
                    elif 0 < graph[y + dy][x + dx] < cur_size:
                        visited[y + dy][x + dx] = visited[y][x] + 1
                        fishOne.append((y + dy, x + dx, visited[y + dy][x + dx] - 1))
                    ## 물고기 존재 but 같은 경우 -> 지나갈 수만
                    elif graph[y + dy][x + dx] == cur_size:
                        visited[y + dy][x + dx] = visited[y][x] + 1
                        queue.append((y + dy, x + dx))
    return fishOne

def eatMore():
    fishMore = [] # 물고기 좌표와 시간 넣기
    global time, cur_size, cur_eat, graph, cur_y, cur_x
    visited = [[0 for _ in range(n)] for _ in range(n)]
    queue.append((cur_y, cur_x))
    visited[cur_y][cur_x] = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in move:
            if 0 <= y + dy < n and 0 <= x + dx < n:
                # 방문하지 않는 경우
                if visited[y + dy][x + dx] == 0:
                    ## 물고기 없음
                    if graph[y + dy][x + dx] == 0:
                        visited[y + dy][x + dx] = visited[y][x] + 1
                        queue.append((y + dy, x + dx))
                    ## 잡아먹을 수 있는 물고기
                    elif 0 < graph[y + dy][x + dx] < cur_size:
                        visited[y + dy][x + dx] = visited[y][x] + 1
                        fishMore.append((y + dy, x + dx, visited[y + dy][x + dx] - 1))
                    ## 물고기 존재 but 같은 경우 -> 지나갈 수만
                    elif graph[y + dy][x + dx] == cur_size:
                        visited[y + dy][x + dx] = visited[y][x] + 1
                        queue.append((y + dy, x + dx))
    if len(fishMore) >= 2:
        fishMore = sorted(fishMore, key = lambda x : (x[2], x[0], x[1]))
    # print("여러개 물고기 잡을 수 있는 경우에서 좌표, 거리")
    # print(fishMore)
    return fishMore

# print("처음 그래프")
# for cow in graph:
#     print(cow)

## 먹을 수 있는 경우
while eatFlag():
    ## 먹을 수 있는 물고기 == 1마리
    if len(fish_index) == 1:
        fishOne = eatOne()
        if len(fishOne) != 0:
            cur_y, cur_x = fishOne[0][0], fishOne[0][1]
            graph[cur_y][cur_x] = 0
            cur_eat += 1
            if cur_size == cur_eat:
                cur_size += 1
                cur_eat = 0
            #     print("몸 크기 증가", cur_size)
            # print("now time", fishOne[0][2])
            time += fishOne[0][2]
            # print("total time", time)
    ## 먹을 수 있는 물고기 > 1마리
    else:
        fishMore = eatMore()
        ## 잡아 먹어야 함
        if len(fishMore) != 0:
            cur_y, cur_x = fishMore[0][0], fishMore[0][1]
            graph[cur_y][cur_x] = 0
            # print("now time", fishMore[2])
            time += fishMore[0][2]
            # print("total time", time)
            cur_eat += 1
            if cur_size == cur_eat:
                cur_size += 1
                cur_eat = 0
        #         print("몸 크기 증가", cur_size)
    # print("잡아먹은 후 좌표")
    # print(cur_y, cur_x)
    # for cow in graph:
    #     print(cow)
    # print()

print(time)





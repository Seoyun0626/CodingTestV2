# 1. 비어 있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리
# 2. 칸이 여러개 -> 비어있는 칸이 가장 많은 칸
# 3. 행 번호 가장 작고, 열 번호 가장 작은 자리

## 가능한 자리(행, 열, 비어있는 칸)

n = int(input())
info = []
graph = [[0 for _ in range(n)] for _ in range(n)]
move = [[0, -1], [1, 0], [0, 1], [-1, 0]]
visited = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n * n):
    info.append(list(map(int, input().split())))
# print(info)

## 가능한 자리 찾기
def findSeat(graph, tmp_seat, love):
    for y in range(len(graph)):
        for x in range(len(graph)):
            if visited[y][x] == 1:
                continue
            love_cnt = 0
            blank_cnt = 0
            for dy, dx in move:
                if 0 <= y + dy < n and 0 <= x + dx < n:
                    if graph[y + dy][x + dx] in love:
                        love_cnt += 1
                    elif graph[y + dy][x + dx] == 0:
                        blank_cnt += 1
            tmp_seat.append((y, x, love_cnt, blank_cnt))
    tmp_seat = sorted(tmp_seat, key = lambda x : (-x[2], -x[3], x[0], x[1]))
    return tmp_seat[0]


## 자리 배치
for i in range(n * n):
    num, *love = info[i]
    tmp_seat = []
    y, x, love_cnt, blank_cnt = findSeat(graph, tmp_seat, love)
    graph[y][x] = num
    visited[y][x] = 1

## info 정렬
info = sorted(info, key = lambda x : x[0])

## 만족도 구하기
answer = 0
for y in range(len(graph)):
    for x in range(len(graph)):
        cnt = 0
        for dy, dx in move:
            if 0 <= dy + y < n and 0 <= dx + x < n:
                if graph[y + dy][x + dx] in info[graph[y][x] - 1][1:]:
                    cnt += 1
        if cnt != 0:
            answer += (10 ** (cnt - 1))
print(answer)



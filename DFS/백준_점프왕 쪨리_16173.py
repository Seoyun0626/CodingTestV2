# 이동 가능 방향 : 오른쪽 / 아래
# 놓친 Point : 움직일 수 있는 숫자가 0인 경우
n = int(input())
visited = [[False for i in range(n)] for j in range(n)]
flag = 0
# print(visited)

graph = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
# print(graph)

## DFS 구현
def dfs(x, y):
    global n
    global flag
    ## 예외 처리 - 게임 구역 크기 초과
    if x >= n or y >= n:
        return
    visited[y][x] = True
    ## 도착하는 경우
    if graph[y][x] == -1:
        # print("finish", y, x)
        flag = 1
        return
    move = graph[y][x]
    ## 0인경우 예외 처리
    if move == 0:
        return
    dfs(x, y+move) # 아래로 이동하는 경우
    dfs(x+move, y) # 오른쪽으로 이동하는 경우

dfs(0,0)
if flag == 1:
    print("HaruHaru")
else:
    print("Hing")




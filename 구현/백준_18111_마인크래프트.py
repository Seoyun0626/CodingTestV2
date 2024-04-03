import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
## 높이별 땅의 개수
graph = [0] * 257
time = sys.maxsize - 1
height = 0

## 시간 구하는 함수
def solution(goal):
    # 추가 블록
    need = 0
    # 제거 블록
    remove = 0
    for i in range(257):
        # i = 현재 높이
        # 현재 높이의 개수, 만드려는 높이 차
        current_num, diff = graph[i], i - goal
        if current_num == 0:
            continue
        ## 블록을 추가해야함
        if diff < 0:
            need += (-diff) * current_num
        ## 블록 제거
        else:
            remove += (diff) * current_num
    if remove + b >= need:
        time = need + 2 * remove
        return time
    else:
        return sys.maxsize


## 땅에 대한 높이를 2차원 배열이 아닌 1차원 배열로 만들기
for i in range(n):
    for j in list(map(int, input().split())):
        graph[j] += 1
# print(graph)

for goal in range(257):
    time_value = solution(goal)
    if time >= time_value:
        time = time_value
        height = goal
print(time, height)





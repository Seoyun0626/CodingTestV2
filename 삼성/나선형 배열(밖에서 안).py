# 나선형 배열
## 밖에서 안
### move_count와 dis 필요 없음

def solution(n):
    if n == 1:
        return [[1]]

    answer = [[0 for i in range(n)] for j in range(n)]

    # 0,0에서 시작
    x = 0
    y = 0
    d_idx = 0

    for i in range(n * n):
        answer[y][x] = i + 1
        if d_idx == 0:
            x += 1
            if x == n - 1 or answer[y][x + 1] != 0: # 맨 끝 도달 or 가려는 곳에 이미 값이 있는 경우
                d_idx = 1
        elif d_idx == 1:
            y += 1
            if y == n - 1 or answer[y + 1][x] != 0:
                d_idx = 2
        elif d_idx == 2:
            x -= 1
            if x == 0 or answer[y][x - 1] != 0:
                d_idx = 3
        elif d_idx == 3:
            y -= 1
            if y == 0 or answer[y - 1][x] != 0:
                d_idx = 0
    return answer

arr = solution(5)
for cow in arr:
    print(cow)



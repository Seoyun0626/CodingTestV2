from collections import deque

N, M, R = map(int, input().split())

arr = []
new_arr = [[0] * M for _ in range(N)]
q = deque()

for i in range(N):
    arr.append(list(map(int,input().split())))

## 2차원 배열 -> 1차원 배열(껍질 분리)
loops = min(N, M) // 2 # 껍질 개수
for i in range(loops):
    q.clear()
    q.extend(arr[i][i:M - i]) # 위쪽
    q.extend([row[M - i - 1] for row in arr[i + 1:N - i - 1]]) # 오른쪽
    q.extend(arr[N - i - 1][i:M - i][::-1]) # 아래쪽, 시계방향으로 1차원 배열 넣기 때문에 -> 역으로 재정렬
    q.extend([row[i] for row in arr[i + 1:N - i - 1]][::-1]) # 왼쪽

    # 양수 -> 시계방향 회전 / 음수 -> 시계 반대방향 회전
    q.rotate(-R)

    ## 1차원 배열 -> 2차원 배열
    for j in range(i, M - i):  # 상
        new_arr[i][j] = q.popleft()
    for j in range(i + 1, N - i - 1):  # 우
        new_arr[j][M - i - 1] = q.popleft()
    for j in range(M - i - 1, i - 1, -1):  # 하
        new_arr[N - i - 1][j] = q.popleft()
    for j in range(N - i - 2, i, -1):  # 좌
        new_arr[j][i] = q.popleft()
for cow in new_arr:
    print(cow)
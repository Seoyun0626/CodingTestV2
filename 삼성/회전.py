# zip() 활용한 회전 - 정사각형, 직사각형 모두 적용 가능
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(arr)

## zip 활용
### 시계 방향 90 (=반시계 방향 270)
arr_90 = list(map(list, zip(*arr[::-1])))
print(arr_90)

### 시계 방향 180 (=반시계 방향 180)
arr_180 = [a[::-1] for a in arr[::-1]]
print(arr_180)

### 시계 방향 270 (=반시계 방향 90)
arr_270 = [x[::-1] for x in list(map(list, zip(*arr[::-1])))]
print(arr_270)


## 인덱스 규칙 찾아서 회전
### 정사각형
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = 3
### 시계 방향 90 (=반시계 방향 270)
new_90 = [[0] * n for _ in range(n)]
for y in range(n):
    for x in range(n):
        new_90[x][n - y - 1] = arr[y][x]
print(new_90)

### 시계 방향 180 (=반시계 방향 180)
new_180 = [[0] * n for _ in range(n)]
for y in range(n):
    for x in range(n):
        new_180[n - y - 1][n - x - 1] = arr[y][x]
print(new_180)

### 시계 방향 270 (=반시계 방향 90)
new_270 = [[0] * n for _ in range(n)]
for y in range(n):
    for x in range(n):
        new_270[n - x - 1][y] = arr[y][x]
print(new_270)

### 직사각형
### 시계 방향 90
def rotated_90(a):
    m = len(a)
    n = len(a[0])
    result = [[0] * m for _ in range(n)] # 배열의 가로,세로 길이가 뒤바뀌는 것 주의!
    for y in range(m):
        for x in range(n):
            result[x][m - y - 1] = arr[y][x]
    return result

### 시계 방향 180
def rotated_180(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            result[n - y - 1][m - x - 1] = a[y][x]
    return result

### 시계 방향 270
def rotated_270(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for y in range(n):
        for x in range(m):
            result[m - 1 - x][y] = a[y][x]

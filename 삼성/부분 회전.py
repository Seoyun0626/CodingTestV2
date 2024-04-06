# 7X7 배열
arr = [[7 * j + i for i in range(1, 8)] for j in range(7)]
new_arr = [[0] * 7 for _ in range(7)]
# 시작좌표 + 정사각형 한 변 길이
sy, sx = 2, 2
length = 3

# 배열의 특정 부분(정사각형)회전
def rotate_90(sy, sx, length):
    global arr, new_arr
    for y in range(sy, sy + length):
        for x in range(sx, sx + length):
            ## 1단계 : (0, 0)으로 옮겨주는 변환
            oy, ox = y - sy, x - sx
            ## 2단계 : 90도 회전했을 때 좌표
            ry, rx = ox, length - oy - 1
            ## 3단계 : 다시 (sy, sx)더해 줌
            new_arr[sy + ry][sx + rx] = arr[y][x]
    # new_arr 값을 board에 옮기기
    for y in range(sy, sy + length):
        for x in range(sx, sx + length):
            arr[y][x] = new_arr[y][x]
rotate_90(sy, sx, length)
for cow in arr:
    print(cow)

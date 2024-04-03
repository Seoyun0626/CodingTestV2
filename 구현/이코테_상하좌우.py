# 가장 왼쪽 위 좌표 (1, 1) / 가장 오른쪽 아래 좌표 (n, n)
# n = 5 / plans = "R R R U D D"
n = int(input())
plans = input().split()
x, y = 1, 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direction = ["R", "L", "D", "U"]

for plan in plans:
    for i in range(len(direction)):
        if plan == direction[i]:
            move_x = x + dx[i]
            move_y = y + dy[i]
        if move_x < 1 or move_x > n or move_y < 1 or move_y > n:
            continue
        x, y = move_x, move_y
print(x, y)

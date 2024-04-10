def solution(n):
    if n == 1:
        return [[1]]

    answer = [[0] * n for _ in range(n)]

    x = 0
    y = 0
    d_idx = 0

    for i in range(n * n):
        answer[y][x] = i + 1
        if d_idx == 0:
            y += 1
            if y == n - 1 or answer[y + 1][x] != 0:
                d_idx = 1
        elif d_idx == 1:
            x += 1
            if x == n - 1 or answer[y][x + 1] != 0:
                d_idx = 2
        elif d_idx == 2:
            y -= 1
            if y == 0 or answer[y - 1][x] != 0:
                d_idx = 3
        elif d_idx == 3:
            x -= 1
            if x== 0 or answer[y][x - 1] != 0:
                d_idx = 0
    return answer
answer = solution(4)

for cow in answer:
    print(cow)


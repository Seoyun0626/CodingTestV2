n = int(input())
move = [(0, -1), (0, 1), (1, 0), (-1, 0)]
graph = [[0] * n for _ in range(n)]
info = []
result = 0
for _ in range(n * n):
    info.append(list(map(int, input().split())))

for i in range(n * n):
    num_like = info[i]
    tmp = []
    for y in range(n):
        for x in range(n):
            num_cnt = 0
            blank_cnt = 0
            if graph[y][x] != 0:
                continue
            for dy, dx in move:
                if 0 <= y + dy < n and 0 <= x + dx < n:
                    if graph[y + dy][x + dx] == 0:
                        blank_cnt += 1
                    elif (graph[y + dy][x + dx] in num_like[1:]):
                        num_cnt += 1
            tmp.append((y, x, num_cnt, blank_cnt))
    tmp = sorted(tmp, key = lambda x : (-x[2], -x[3], x[0], x[1]))
    y = tmp[0][0]
    x = tmp[0][1]
    graph[y][x] = num_like[0]

info.sort()
# print(info)
## 만족도 구하기
for y in range(n):
    for x in range(n):
        result_cnt = 0
        num = graph[y][x]
        for dy, dx in move:
            if 0 <= y + dy < n and 0 <= x + dx < n:
                if (graph[y + dy][x + dx] in info[num - 1]):
                    result_cnt += 1
        if result_cnt != 0:
            result += 10 ** (result_cnt - 1)
print(result)








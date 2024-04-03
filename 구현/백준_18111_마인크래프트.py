# 세로(y), 가로(x)
# 땅의 높이 일정하게 바꾸기
# 블록 제거 -> 2초, 블록 쌓기 -> 1초
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
graph = []
dic = {}
for _ in range(n):
    graph.append(list(map(int, input().split())))
# print(graph)

for goal in range(0, 256):
    time = 0
    block = b
    flag = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == goal:
                continue
            ## 블록이 많아서 제거
            elif graph[y][x] > goal:
                remove_block = graph[y][x] - goal
                block += remove_block
                time += (2 * remove_block)
            else:
                more_block = goal - graph[y][x]
                if more_block > block:
                    flag = 1
                    break
                block -= more_block
                time += (1 * more_block)
    if flag == 1:
        break
    else:
        dic[goal] = time
dic = dict(sorted(dic.items(), key = lambda x : x[1]))
result = list(dic.items())[0]
print(result[1], result[0])



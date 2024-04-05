from copy import deepcopy
n = int(input())
result = []
graph = []
for _ in range(n):
    graph.append(list(map(str, input())))
# print(graph)

# 사탕의 색이 다른 구역 리스트에 넣기
diff_color = [] # (x, y / x`, y`)
for y in range(n):
    i = 0
    while i < (n - 1): # 2
        if graph[y][i] != graph[y][i + 1]:
            diff_color.append((i, y, i + 1, y))
        i += 1
for x in range(n):
    j = 0
    while j < (n - 1):
        if graph[j][x] != graph[j + 1][x]:
            diff_color.append((x, j, x, j + 1))
        j += 1
# print(diff_color)

# 사탕 개수세는 함수
def candy_cnt(new_graph):
    # for cow in new_graph:
    #     print(cow)
    # print("end")
    # 가로에서 최대 개수
    max1 = 0
    tmp_result = []
    for y in range(n):
        tmp_cnt = 1
        color = new_graph[y][0]
        for x in range(1, n - 1):
            if color == new_graph[y][x]:
                tmp_cnt += 1
            else:
                tmp_result.append(tmp_cnt)
                tmp_cnt = 1
                color = new_graph[y][x]
        if color == new_graph[y][n - 1]:
            tmp_cnt += 1
            tmp_result.append(tmp_cnt)
        else:
            tmp_result.append(tmp_cnt)
    # print(tmp_result)
    for x in range(n):
        tmp_cnt = 1
        color = new_graph[0][x]
        for y in range(1, n - 1):
            if color == new_graph[y][x]:
                tmp_cnt += 1
            else:
                tmp_result.append(tmp_cnt)
                tmp_cnt = 1
                color = new_graph[y][x]
        if color == new_graph[n - 1][x]:
            tmp_cnt += 1
            tmp_result.append(tmp_cnt)
        else:
            tmp_result.append(tmp_cnt)
    # print(tmp_result)
    tmp_answer = max(tmp_result)
    return tmp_answer

# 사탕 뒤집기
def change_graph(x1, y1, x2, y2, tmp_graph):
    tmp_color = tmp_graph[y1][x1]
    tmp_graph[y1][x1] = tmp_graph[y2][x2]
    tmp_graph[y2][x2] = tmp_color
    return tmp_graph


# diff_color 보면서 돌리기
for x1, y1, x2, y2 in diff_color:
    tmp_graph = deepcopy(graph)
    new_graph = change_graph(x1, y1, x2, y2, tmp_graph)
    cnt = candy_cnt(new_graph)
    result.append(cnt)
if len(result):
    print(max(result))
else:
    print(0)

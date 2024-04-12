# 1번 행과 N번행 연결 / 1번 열과 N번열 연결
# 이동 명령
## 1. d 방향, s 속력
## 2. 같은 칸에 여러 개의 파이어볼 존재 가능
## 2-1. 같은 칸 파이어볼 하나로 합
## 2-2. 4개로 나누어짐
## 3-1. 이때 질량 : sum(질량) / 5 이때 속력 : sum(속력) / sum(파이어볼 개수)
## 3-2. 파이어볼 방향 모두 홀수 or 짝수 : 0, 2, 4, 6 / 그렇지 않으면 1, 3, 5, 7
## 4. 질량이 0 -> 소멸
# k번 명령 후 남아있는 파이어볼 질량 합

move = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
n, m ,k = map(int, input().split())
info = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    info[r - 1][c - 1].append([m, s, d])

# print("파이어볼 정보")
# for cow in info:
#     print(cow)
# print()

for _ in range(k):
    graph = [[[] for _ in range(n)] for _ in range(n)]
    # 모든 파이어볼 이동시키기
    for y in range(n):
        for x in range(n):
            if len(info[y][x]) == 0:
                continue
            for tmp_info in info[y][x]:
                m, s, d = tmp_info[0], tmp_info[1], tmp_info[2]
                ny = (y + move[d][0] * s) % n
                nx = (x + move[d][1] * s) % n
                graph[ny][nx].append([m, s, d])
    # print("이동 후 파이어볼 위치")
    # for cow in graph:
    #     print(cow)

    ## 파이어볼이 여러개 이면 나누기
    info = [[[] for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if len(graph[y][x]) >= 2:
                nm, ns, nd, cnt = 0, 0, [], 0
                for tmp_info in graph[y][x]:
                    nm += tmp_info[0]
                    ns += tmp_info[1]
                    nd.append(tmp_info[2] % 2)
                    cnt += 1
                nm = nm // 5
                graph[y][x] = []
                if nm == 0:
                    continue
                ns = ns // cnt
                nd = len(set(nd))
                if nd == 1:
                    graph[y][x].append([nm, ns, 0])
                    graph[y][x].append([nm, ns, 2])
                    graph[y][x].append([nm, ns, 4])
                    graph[y][x].append([nm, ns, 6])
                else:
                    graph[y][x].append([nm, ns, 1])
                    graph[y][x].append([nm, ns, 3])
                    graph[y][x].append([nm, ns, 5])
                    graph[y][x].append([nm, ns, 7])

    info = [tmp for tmp in graph]

    # print("분리 후 파이어볼 위치")
    # for cow in info:
    #     print(cow)

result = 0
for y in range(n):
    for x in range(n):
        if len(info[y][x]) == 0:
            continue
        for tmp_info in info[y][x]:
            result += tmp_info[0]
print(result)





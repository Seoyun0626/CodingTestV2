# 세로(y), 가로(x)
n, m = map(int, input().split())
graphA = []
graphB = []
for _ in range(n):
    graphA.append(list(map(int, input().split())))
# print(graphA)
# for cowA in graphA:
#     print(cowA)
# 세로(y), 가로(x)
m, k = map(int, input().split())
result = [[] for _ in range(n)]
for _ in range(m):
    graphB.append(list(map(int, input().split())))
# print(graphB)
# for cosB in graphB:
#     print(cosB)
# print(result)

for y in range(n): # 3
    for x in range(k): # 2
        num = 0
        for z in range(m): # 2
            num += (graphA[y][z]*graphB[z][x])
        # print(num)
        result[y].append(num)
for cow in result:
    print(*cow)
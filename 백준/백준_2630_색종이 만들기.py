import sys
input = sys.stdin.readline

n = int(input())
length = n // 2
blue = 0
white = 0
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# print(graph)


def check(y, x, n):
    global blue, white
    color = graph[y][x]
    for i in range(y, y + n):
        for j in range(x, x + n):
            ## 다른색 -> 쪼개기
            if graph[i][j] != color:
                check(y, x, n // 2) # 1사분면
                check(y, x + n // 2, n // 2) # 2사분면
                check(y + n // 2, x, n // 2) # 3사분면
                check(y + n // 2, x + n // 2, n // 2) # 4사분면
                return
    if color == 1:
        blue += 1
    else:
        white += 1

check(0, 0, n)
print(white)
print(blue)





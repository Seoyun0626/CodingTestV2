from collections import deque
import sys
input = sys.stdin.readline

move = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

def bfs(cur_x, cur_y, final_x, final_y):
    queue = deque()
    queue.append((cur_x, cur_y))
    global graph

    while queue:
        x, y = queue.popleft()
        # print("x:",x, "y:", y)
        for dy, dx in move:
            if x + dx == final_x and y + dy == final_y:
                graph[y+dy][x+dx] = graph[y][x] + 1
                return graph[y+dy][x+dx]
            elif 0 <= x + dx < n and 0 <= y + dy < n:
                if graph[y+dy][x+dx] == 0:
                    queue.append((x + dx, y + dy))
                    graph[y+dy][x+dx] = graph[y][x] + 1
                    # print(x+dx, y+dy)

t = int(input())
for _ in range(t):
    n = int(input())
    cur_x, cur_y = map(int, input().split())
    graph = [[0 for i in range(n)] for j in range(n)]
    final_x, final_y = map(int, input().split())
    if cur_x == final_x and cur_y == final_y:
        print(0)
    else:
        answer = bfs(cur_x, cur_y, final_x, final_y)
        print(answer)
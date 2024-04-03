# i == y, j == x
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
matrix = []
result = 0
for _ in range(n):
    matrix.append(list(map(int, input().split())))
# for cow in matrix:
    # print(cow)
k = int(input())
for _ in range(k):
    result = 0
    left_y, left_x, right_y, right_x = map(int, input().split())
    for y in range(left_y - 1, right_y):
        result += sum(matrix[y][left_x - 1:right_x])
    print(result)
# i == y, j == x
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
k = int(input())
do = [list(map(int, input().split())) for _ in range(k)]
# print(do)

dp = [[0 for i in range(m + 1)] for _ in range(n + 1)]
for y in range(1, n + 1):
    for x in range(1, m + 1):
        dp[y][x] = dp[y - 1][x] + dp[y][x - 1] - dp[y - 1][x - 1] + matrix[y - 1][x - 1]

for _, line in enumerate(do):
    j, i, y, x = line
    print(dp[y][x] - (dp[y][i - 1] + dp[j - 1][x]) + dp[j - 1][i - 1])
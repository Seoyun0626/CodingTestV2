dp = [0] * 100
dp[0] = 1
dp[1] = 1
dp[2] = 1

t = int(input())
for _ in range(t):
    n = int(input())
    n = n - 1
    if n <= 2:
        result = 1
    else:
        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2]
        result = dp[n]
    print(result)

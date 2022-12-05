N = int(input())
dp = [[0]*10 for _ in range(N+1)]

dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, N+1):
    dp[i][9] = 1
    for j in range(8, -1, -1):
        dp[i][j] = dp[i-1][j] + dp[i][j+1]

print(sum(dp[N])%10007)
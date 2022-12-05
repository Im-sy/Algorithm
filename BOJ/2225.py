N, K = map(int, input().split())
dp = [[0]*N for _ in range(K)]
dp[0] = [1]*N
for i in range(1, K):
    dp[i][0] = i+1
    for j in range(1, N):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j])%1000000000
print(dp[K-1][N-1]%1000000000)
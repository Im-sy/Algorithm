N = int(input())

dp = [0]*(N+1)
dp[0] = 1
dp[1] = 3
if N >= 2:
    for i in range(2, N+1):
        dp[i] = (2*dp[i-1] + dp[i-2])%9901
print(dp[N])


# 0: 빈 우리, 1: 왼쪽에 사자, 2: 오른쪽에 사자
dp = [[0, 0, 0] for _ in range(N+1)]
dp[1] = [1, 1, 1]
for i in range(2, N+1):
    dp[i][0] = sum(dp[i-1])%9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2])%9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1])%9901
print(sum(dp[N])%9901)
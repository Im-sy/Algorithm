import sys
input = sys.stdin.readline
N, K = map(int, input().split())
objects =[[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if objects[i][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            # i번째를 챙기지 않았을 때와 챙겼을 때 중 최대값
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-objects[i][0]] + objects[i][1])
# for row in dp:
#     print(row)
print(dp[N][K])
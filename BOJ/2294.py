import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)])

dp = [10001]*(k+1)
dp[0] = 0
for i in coins:
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j-i]+1)

if dp[-1]>10000:
    print(-1)
else:
    print(dp[-1])
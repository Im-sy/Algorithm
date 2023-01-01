import sys
input = sys.stdin.readline

n = int(input())
wines = [int(input()) for _ in range(n)]

dp = [0]*n
if n == 1:
    print(wines[0])
elif n == 2:
    print(wines[0]+wines[1])
else:
    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    dp[2] = max(wines[0]+wines[2], wines[1]+wines[2], dp[1])
    for i in range(3, n):
        dp[i] = max(wines[i] + wines[i-1] + dp[i-3], wines[i] + dp[i-2], dp[i-1])
    print(dp[-1])
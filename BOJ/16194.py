import sys
input = sys.stdin.readline

N = int(input())
card = [0] + list(map(int, input().split()))

dp = [0]*(N+1)
for i in range(1, N+1):
    min_tmp = 9999999
    for j in range(1, i+1):
        min_tmp = min(min_tmp, dp[i-j]+card[j])
    dp[i] = min_tmp

print(dp[-1])
import sys
input = sys.stdin.readline

N = int(input())
arrs = [list(map(int, input().split())) for _ in range(N)]
arrs.sort(key=lambda x : x[0])

dp = [1]*N
for i in range(N):
    for j in range(i):
        if arrs[i][1] > arrs[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(N - max(dp))
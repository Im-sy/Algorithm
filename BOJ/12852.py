N = int(input())

def dfs(n, cnt, p):
    global ans, path
    if ans < cnt:
        return
    if n == 1:
        if ans > cnt:
            ans = cnt
            path = p
        return
    if n % 3 == 0:
        dfs(n//3, cnt+1, p+[n//3])
    if n % 2 == 0:
        dfs(n//2, cnt+1, p+[n//2])
    dfs(n-1, cnt+1, p+[n-1])

ans = 10**6
path = []
dfs(N, 0, [N])
print(ans)
print(*path)

##########################

dp = [[0, []] for _ in range(N + 1)]

for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][0] + 1
    dp[i][1] = dp[i - 1][1] + [i]
    if i % 3 == 0 and dp[i // 3][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 3][0] + 1
        dp[i][1] = dp[i // 3][1] + [i]
    if i % 2 == 0 and dp[i // 2][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = dp[i // 2][1] + [i]

print(dp[-1][0])
print(*(dp[-1][1][::-1] + [1]))
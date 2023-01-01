def dfs(n, cnt):
    global ans
    if ans < cnt:
        return
    if n == 1:
        if ans > cnt:
            ans = cnt
        return
    if n % 3 == 0:
        dfs(n//3, cnt+1)
    if n % 2 == 0:
        dfs(n//2, cnt+1)
    dfs(n-1, cnt+1)

import sys
N = int(sys.stdin.readline())
ans = 10**6
dfs(N, 0)
print(ans)
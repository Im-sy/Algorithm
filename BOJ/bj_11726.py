# 시간 초과
import sys
sys.setrecursionlimit(10**6)
def solve(n):
    global ans
    if n > N:
        return
    if n == N:
        ans += 1
        return
    solve(n+1)
    solve(n+2)

N = int(input())
# ans = 0
# solve(0)
# print(ans%10007)
ans = [0]*(N+1)
ans[0] = 1
ans[1] = 1
for i in range(2, N+1):
    ans[i] = (ans[i-2] + ans[i-1])%10007
print(ans[N])
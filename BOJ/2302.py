import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
vip = [int(input().strip()) for _ in range(M)]
# print(vip)

dp = [0]*(N+1)
dp[0] = 1
dp[1] = 1
for i in range(2, N+1):
    dp[i] = dp[i-2] + dp[i-1]

# ans = 1
# tmp = 0
# for i in range(M):
#     ans *= dp[vip[i]-1-tmp]
#     tmp = vip[i]
# ans *= dp[N-tmp]

ans = 1
cnt = []
tmp = 0
for i in range(1, N+1):
    if i in vip:
        # cnt.append(tmp)
        ans *= dp[tmp]
        tmp = 0
    else:
        tmp += 1
# cnt.append(tmp)
ans *= dp[tmp]
# print(cnt)
# for x in cnt:
#     ans *= dp[x]

print(ans)
import sys
input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1
for r in range(N):
    for c in range(N):
        if r == N-1 and c == N-1 :
            print(dp[r][c])
            break
        for dr, dc in [(0, 1), (1, 0)]:
            nr = r + dr*maps[r][c]
            nc = c + dc*maps[r][c]
            if 0<=nr<N and 0<=nc<N:
                dp[nr][nc] += dp[r][c]

# for row in dp:
#     print(row)
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
heights = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(i, j, k):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        ci, cj = q.popleft()
        for l in range(4):
            ni = ci + dr[l]
            nj = cj + dc[l]
            if 0<=ni<N and 0<=nj<N and heights[ni][nj]>=k and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))

max_height = max(map(max, heights))
min_height = min(map(min, heights))
ans = min_height
for k in range(min_height, max_height+1):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if heights[r][c]>=k and not visited[r][c]:
                bfs(r, c, k)
                cnt += 1
    ans = max(ans, cnt)

print(ans)
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c):
    q = deque([(r, c, 0)])
    v = [[0]*M for _ in range(N)]
    v[r][c] = 1
    res = -1
    while q:
        cr, cc, cnt = q.popleft()
        res = max(res, cnt)
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0<=nr<N and 0<=nc<M and arr[nr][nc]=='L' and not v[nr][nc]:
                q.append((nr, nc, cnt+1))
                v[nr][nc] = 1
    return res

ans = -1
for r in range(N):
    for c in range(M):
        if arr[r][c] == 'L':
            ans = max(ans, bfs(r, c))

print(ans)
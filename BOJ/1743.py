import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c):
    q = deque([(r, c)])
    maps[r][c] = 0
    cnt = 1
    while q:
        cr, cc = q.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0<nr<=N and 0<nc<=M and maps[nr][nc]:
                q.append((nr, nc))
                maps[nr][nc] = 0
                cnt += 1
    return cnt


N, M, K = map(int, input().split())
maps = [[0]*(M+1) for _ in range(N+1)]
for _ in range(K):
    a, b = map(int, input().split())
    maps[a][b] = 1
ans = 0
for r in range(1, N+1):
    for c in range(1, M+1):
        if maps[r][c]:
            ans = max(ans, bfs(r, c))
print(ans)
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

q = deque()
v = [[0]*M for _ in range(N)]
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            q.append((r, c))
            v[r][c] = 1

while q:
    cr, cc = q.popleft()
    for k in range(8):
        nr = cr + dr[k]
        nc = cc + dc[k]
        if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 0 and not v[nr][nc]:
            q.append((nr, nc))
            v[nr][nc] = v[cr][cc] + 1

ans = 0
for r in range(N):
    for c in range(M):
        if v[r][c] > ans:
            ans = v[r][c]
print(ans-1)
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arts = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def bfs(r, c):
    q = deque([(r, c)])
    arts[r][c] = 0
    tmp = 1
    while q:
        cr, cc = q.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0<=nr<n and 0<=nc<m and arts[nr][nc] == 1:
                q.append((nr, nc))
                arts[nr][nc] = 0
                tmp += 1
    return tmp

ans = 0
cnt = 0
for r in range(n):
    for c in range(m):
        if arts[r][c] == 1:
            ans = max(ans, bfs(r, c))
            cnt += 1
print(cnt)
print(ans)
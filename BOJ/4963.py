import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
def bfs(r, c):
    q = deque([(r, c)])
    maps[r][c] = 0
    while q:
        cr, cc = q.popleft()
        for k in range(8):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0<=nr<h and 0<=nc<w and maps[nr][nc]:
                q.append((nr, nc))
                maps[nr][nc] = 0

while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    maps = [list(map(int, input().split())) for _ in range(h)]
    ans = 0
    for r in range(h):
        for c in range(w):
            if maps[r][c] == 1:
                bfs(r, c)
                ans += 1
    print(ans)
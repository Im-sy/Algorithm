import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0 ,-1]
def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = 1
    union = [(r, c)]
    while q:
        cr, cc = q.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and L <= abs(population[nr][nc] - population[cr][cc]) <= R:
                q.append((nr, nc))
                visited[nr][nc] = 1
                union.append((nr, nc))
    tmp, cnt = 0, 0
    for ur, uc in union:
        tmp += population[ur][uc]
        cnt += 1
    if cnt > 1:
        for ur, uc in union:
            population[ur][uc] = tmp // cnt
        return True
    else:
        return False

ans = 0
while True:
    visited = [[0]*N for _ in range(N)]
    flag = False
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and bfs(r, c):
                flag = True
    if not flag:
        break
    ans += 1
print(ans)
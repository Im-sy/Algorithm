import sys
from copy import deepcopy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

v = []
w = []
for r in range(N):
    for c in range(M):
        if map[r][c] == 2:
            v.append((r, c))
        elif map[r][c] == 0:
            w.append((r, c))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def bfs(virus, walls, map):
    graph = deepcopy(map)
    for i, j in walls:
        graph[i][j] = 1
    q = deque(virus)
    while q:
        cr, cc = q.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0<=nr<N and 0<=nc<M and graph[nr][nc]==0:
                graph[nr][nc] = 2
                q.append((nr, nc))
    cnt = 0
    for r in range(N):
        for c in range(M):
            if graph[r][c] == 0:
                cnt += 1
    return cnt

ans = 0
for comb in combinations(w, 3):
    ans = max(ans, bfs(v, list(comb), map))
print(ans)
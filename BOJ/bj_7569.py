from collections import deque
# 위 아래 앞 우 뒤 좌
dz = [1, -1, 0, 0, 0, 0]
dr = [0, 0, -1, 0, 1, 0]
dc = [0, 0, 0, 1, 0, -1]

import sys
M, N, H = map(int, input().split())
# 3차원 토마토
tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
# print(tomato)
queue = deque()
# z:층, r:행, c:열
for z in range(H):
    for r in range(N):
        for c in range(M):
            if tomato[z][r][c] == 1:
                queue.append((z, r, c, 0))
# print(queue)
# BFS 수행
while queue:
    cz, cr, cc, d = queue.popleft()
    for k in range(6):
        nz = cz + dz[k]
        nr = cr + dr[k]
        nc = cc + dc[k]
        if 0<=nz<H and 0<=nr<N and 0<=nc<M and tomato[nz][nr][nc] == 0:
            queue.append((nz, nr, nc, d+1))
            tomato[nz][nr][nc] = 1

# BFS 완료 했는데도 안 익은 토마토(0) 있다면 -1 반환
for z in range(H):
    for r in range(N):
        for c in range(M):
            if tomato[z][r][c] == 0:
                d = -1
                break
print(d)
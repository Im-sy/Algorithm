import sys
from collections import deque
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

q = deque()
# v를 3차원으로 만들기!!!
# 0000
# 0100
# 0000
# 1111
# 0000
# 1을 뚫고 오면 아래 1111 벽 뚫지 못함
# 벽을 뚤지 않고 온 경우(0), 벽을 뚫고 온 경우(1)
v = [[[0]*2 for _ in range(M)] for _ in range(N)]
# BFS 수행
q.append((0, 0, 0, 1))
v[0][0][0] = 1
while q:
    cr, cc, w, d = q.popleft()
    # 끝에 도달했다면 break
    if cr == N-1 and cc == M-1:
        break
    # 상우하좌 방향으로
    for k in range(4):
        nr = cr + dr[k]
        nc = cc + dc[k]
        # 범위 내에 있고 방문하지 않았을 경우
        if 0<=nr<N and 0<=nc<M and not v[nr][nc][w]:
            # 길이 있다면(0)
            if not arr[nr][nc]:
                q.append((nr, nc, w, d+1))
                v[nr][nc][w] = 1
            # 길이 없는데(1) 아직 벽을 부시지 않았다면(w=0)
            if arr[nr][nc] and w == 0:
                # 벽을 부신 상태(w=1)
                q.append((nr, nc, 1, d+1))
                v[nr][nc][w] = 1
else: # 끝에 도달하지 못한 경우
    d = -1
print(d)
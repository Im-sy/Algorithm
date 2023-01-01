dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

import sys
M, N = map(int, input().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
queue = []
# 익은 토마토가 있는 곳 모두 enqueue 해두기
# 행, 열, 날짜 수 enqueue
for r in range(N):
    for c in range(M):
        if tomato[r][c] == 1:
            queue.append((r, c, 0))

# bfs 수행
while queue:
    cr, cc, d = queue.pop(0)
    # 상우하좌 모든 방향에 대해서 익지 않은 토마토의 경우에 탐색
    for k in range(4):
        nr = cr + dr[k]
        nc = cc + dc[k]
        if 0<=nr<N and 0<=nc<M and tomato[nr][nc] == 0:
            # 갈 수 있는 곳을 enqueue할 때 날짜 수 하나 더해주기
            queue.append((nr, nc, d+1))
            tomato[nr][nc] = 1

# dfs를 다 수행했음에도 익지 않은 토마토가 있다면 -1 출력
for r in range(N):
    for c in range(M):
        if tomato[r][c] == 0:
            d = -1
            break
print(d)

# deque 라이브러리 활용
# from collections import deque
# queue = deque()
# for r in range(N):
#     for c in range(M):
#         if tomato[r][c] == 1:
#             queue.append((r, c, 0))
# 
# while queue:
#     cr, cc, d = queue.popleft()
#     for k in range(4):
#         nr = cr + dr[k]
#         nc = cc + dc[k]
#         if 0<=nr<N and 0<=nc<M and tomato[nr][nc] == 0:
#             queue.append((nr, nc, d+1))
#             tomato[nr][nc] = 1
# 
# for r in range(N):
#     for c in range(M):
#         if tomato[r][c] == 0:
#             d = -1
#             break
# print(d)
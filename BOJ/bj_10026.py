dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# from collections import deque
# def bfs(r, c):
#     q.append((r, c))
#     visited[r][c] = 1
#     while q:
#         cr, cc = q.popleft()
#         for k in range(4):
#             nr = cr + dr[k]
#             nc = cc + dc[k]
#             if 0<=nr<N and 0<=nc<N and arr[nr][nc]==arr[cr][cc] and not visited[nr][nc]:
#                 visited[nr][nc] = 1
#                 q.append((nr, nc))

def bfs(r, c):
    visited[r][c] = 1
    cc = arr[r][c]
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0<=nr<N and 0<=nc<N and arr[nr][nc]==cc and not visited[nr][nc]:
            bfs(nr, nc)

import sys
# 재귀 최대한도 설정 pypy에서는 안됨!!
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().strip()) for _ in range(N)]
q = deque()

visited = [[0]*N for _ in range(N)]
cnt1 = 0
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            cnt1 += 1
            bfs(r, c)
        if arr[r][c] == 'R':
            arr[r][c] = 'G'

# print(arr)
# for r in range(N):
#     for c in range(N):
#         if arr[r][c] == 'R':
#             arr[r][c] = 'G'

visited = [[0]*N for _ in range(N)]
cnt2 = 0
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            cnt2 += 1
            bfs(r, c)

print(cnt1, cnt2)
import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().split())
visited = [[0]*M for _ in range(N)]
for _ in range(K):
    s_x, s_y, e_x, e_y = map(int, input().split())
    for x in range(s_x, e_x):
        for y in range(s_y, e_y):
            visited[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    d = 1
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                d += 1
    return d

cnt = 0
d_list = []
for r in range(N):
    for c in range(M):
        if not visited[r][c]:
            d_list.append(bfs(r, c))
            cnt += 1

print(cnt)
print(*sorted(d_list))
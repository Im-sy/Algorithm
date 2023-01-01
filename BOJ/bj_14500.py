import sys
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
def dfs(r, c, tmp, cnt):
    global ans
    if cnt == 4:
        if ans < tmp:
            ans = tmp
        return
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc, tmp+arr[nr][nc], cnt+1)
            visited[nr][nc] = 0

def hhhh(r, c):
    center = arr[r][c]
    w = 4
    min_w = 9999999
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if w == 2:
            return 0
        if not (0<=nr<N and 0<=nc<M):
            w -= 1
            continue
        center += arr[nr][nc]
        if arr[nr][nc] < min_w:
            min_w = arr[nr][nc]
    if w == 4:
        center -= min_w
    return center

for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        dfs(r, c, arr[r][c], 1)
        visited[r][c] = 0
        ans = max(ans, hhhh(r, c))

print(ans)

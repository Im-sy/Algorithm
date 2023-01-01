T = int(input())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# def dfs(cnt, r, c):
#     if r<0 or r>=N or c<0 or c>=N or maze[r][c]=='1':
#         return
#     for k in range(4):
#         nr = r + dr[k]
#         nc = c + dc[k]
#         if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != '1' and not visited[nr][nc]:
#             cnt = dfs(cnt+1, nr, nc)
#     return cnt

def dfs():
    visited = [[0] * N for _ in range(N)]
    stack = [(start[0], start[1], 0)]
    visited[start[0]][start[1]] = 1
    while stack:
        cr, cc, distance = stack.pop()
        if maze[cr][cc] == '3':
            return distance-1
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != '1' and not visited[nr][nc]:
                stack.append((nr, nc, distance+1))
                visited[nr][nc] = 1
    return 0

for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':
                start = (r, c)
                break

    print(f'#{tc} {dfs()}')
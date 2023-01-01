T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    q = [(0, 0)]
    visited = [[9999999]*N for _ in range(N)]
    visited[0][0] = arr[0][0]
    while q:
        cr, cc = q.pop(0)
        for k in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nr = cr + k[0]
            nc = cc + k[1]
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]>visited[cr][cc]+arr[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[cr][cc] + arr[nr][nc]
    print(f'#{tc} {visited[N-1][N-1]}')

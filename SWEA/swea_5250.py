T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    q = [(0, 0)]
    visited = [[0xffffff] * N for _ in range(N)]
    visited[0][0] = 0
    while q:
        cr, cc = q.pop(0)
        for dr, dc, in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < N and 0 <= nc < N:
                diff = 0
                if arr[nr][nc] > arr[cr][cc]:
                    diff = arr[nr][nc] - arr[cr][cc]
                if visited[nr][nc] > visited[cr][cc] + diff + 1:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[cr][cc] + diff + 1

    print(f'#{tc} {visited[N-1][N-1]}')
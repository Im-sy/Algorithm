T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # arr = [list(map(int, input().rstrip('\r')) for _ in range(N)]
    start_r, start_c = 0, 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '2':
                start_r, start_c = r, c
    stack = []
    stack.append((start_r, start_c))
    visited = [[0] * N for _ in range(N)]
    visited[start_r][start_c] = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while stack:
        cr, cc = stack[-1]
        visited[cr][cc] = 1
        if arr[cr][cc] == '3':
            ans = 1
            break
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != '1' and not visited[nr][nc]:
                stack.append((nr, nc))
                break
        else:
            stack.pop()
    else:
        ans = 0
    print(f'#{tc} {ans}')
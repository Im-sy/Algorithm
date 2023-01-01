T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 0, 1, 0, -1, 1, 1, -1]
    dc = [0, 1, 0, -1, 1, 1, -1, -1]
    max_tmp = 0
    for r in range(N):
        for c in range(M):
            s = arr[r][c]
            for k in range(4):
                for l in range(1,M):
                    nr, nc = r + dr[k]*l, c + dc[k]*l
                    if 0<=nr<N and 0<=nc<N:
                        s += arr[nr][nc]
            if max_tmp < s:
                max_tmp = s
            s = arr[r][c]
            for k in range(4, 8):
                for l in range(1,M):
                    nr, nc = r + dr[k]*l, c + dc[k]*l
                    if 0<=nr<N and 0<=nc<N:
                        s += arr[nr][nc]
            if max_tmp < s:
                max_tmp = s
    print(f'#{tc} {max_tmp}')
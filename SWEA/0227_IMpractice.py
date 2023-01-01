T = int(input())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N+1)]
    new_arr = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'A':
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0<=nr<N and 0<=nc<N:
                        new_arr[nr][nc] += 1
            elif arr[r][c] == 'B':
                for l in range(1, 3):
                    for k in range(4):
                        nr = r + dr[k]*l
                        nc = c + dc[k]*l
                        if 0 <= nr < N and 0 <= nc < N:
                            new_arr[nr][nc] += 1
            elif arr[r][c] == 'C':
                for l in range(1, 4):
                    for k in range(4):
                        nr = r + dr[k]*l
                        nc = c + dc[k]*l
                        if 0 <= nr < N and 0 <= nc < N:
                            new_arr[nr][nc] += 1
    cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'H' and not new_arr[r][c]:
                cnt += 1
    print(*new_arr)
    print(f'#{tc} {cnt}')
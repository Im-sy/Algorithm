T = int(input())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    stack = [(r, c, 1)]
    visited = [[0]*N for _ in range(N)]
    visited[r][c] = 1
    while stack:
        cr, cc, d = stack.pop()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0<=nr<N and 0<=nc<N and arr[nr][nc] == arr[cr][cc] + 1 and not visited[nr][nc]:
                stack.append((nr, nc, d+1))
                visited[nr][nc] = 1
    return d

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    for r in range(N):
        for c in range(N):
            ans.append((arr[r][c], dfs(r, c)))
    # max_cnt = max(ans)[0]
    # tmp_min = max(ans)[1]
    # for x in ans:
    #     if x[0] == max_cnt and tmp_min > x[1]:
    #         tmp_min = x[1]
    # print(f'#{tc} {tmp_min} {max_cnt}')
    ans.sort(key=lambda x:(-x[1], x[0]))
    print(f'#{tc} {ans[0][0]} {ans[0][1]}')
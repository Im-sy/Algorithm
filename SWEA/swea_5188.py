def dfs(r, c):
    global total, result
    if total > result:
        return
    if r == N - 1 and c == N - 1:
        if total < result:
            result = total
    for dr, dc in ((0, 1), (1, 0)):
        nr = r + dr
        nc = c + dc
        if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
            visited[nr][nc] = 1
            total += arr[nr][nc]
            dfs(nr, nc)
            visited[nr][nc] = 0
            total -= arr[nr][nc]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    result = 999999
    total = arr[0][0]
    dfs(0, 0)
    print(f'#{tc} {result}')
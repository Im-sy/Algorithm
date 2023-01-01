T = int(input())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c, d, num):
    if d == 6:
        result.append(num)
        return
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0<=nr<4 and 0<=nc<4:
            dfs(nr, nc, d+1, num+arr[nr][nc])

for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    result = []
    for r in range(4):
        for c in range(4):
            dfs(r, c, 0, arr[r][c])
    print(f'#{tc} {len(set(result))}')
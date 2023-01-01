T = int(input())
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

def dfs(cr, cc, d, idx):
    global ans
    if idx < 3:
        tmp = idx + 2
    else:
        tmp = idx + 1

    for k in range(idx, tmp):
        nr = cr + dr[k]
        nc = cc + dc[k]
        if nr == sr and nc == sc:
            if ans < d:
                ans = d
            return
        if 0<=nr<N and 0<=nc<N and not v[arr[nr][nc]]:
            v[arr[nr][nc]] = 1
            dfs(nr, nc, d+1, k)
            v[arr[nr][nc]] = 0

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*101
    ans = -1
    for r in range(N):
        for c in range(N):
            sr, sc = r, c
            v[arr[r][c]] = 1
            dfs(r, c, 1, 0)
            v[arr[r][c]] = 0
    print(f'#{tc} {ans}')



# 유튜브 라이브
def DFS(n, ci, cj, v, cnt):
    global si, sj, ans
    if n==2 and ans>=cnt*2:
        return
    if n>3:
        return
    if ci==si and cj==sj and n==3 and ans<cnt:
        ans = cnt
        return
    for k in range(n, n+2):
        ni, nj = ci + di[k], cj + dj[k]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            DFS(k, ni, nj, v, cnt+1) #v+[arr[ni][nj]]
            v.pop()

# 시계 반대방향
di, dj = (1, 1, -1, -1, 1), (-1, 1, 1, -1, -1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for si in range(0, N-2):
        for sj in range(1, N-1):
            DFS(0, si, sj, [], 0)
    print(f'#{tc} {ans}')
pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
opp = [1, 0, 3, 2]

def BFS(N, M, sr, sc, L):
    q = []
    v = [[0]*M for _ in range(N)]
    q.append((sr, sc))
    v[sr][sc] = 1
    cnt = 1

    while q:
        cr, cc = q.pop(0)
        if v[cr][cc] == L:
            return cnt
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0<=nr<N and 0<=nc<M and not v[nr][nc] and\
                pipe[arr[cr][cc]][k] and pipe[arr[nr][nc]][opp[k]]:
                q.append((nr, nc))
                v[nr][nc] = v[cr][cc] + 1
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = BFS(N, M, R, C, L)
    print(f'#{tc} {ans}')
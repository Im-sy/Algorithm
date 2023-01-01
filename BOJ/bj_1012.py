import sys
# 재귀함수 최대 한도 깊이 때문에 런타임 에러 날 수 있음
sys.setrecursionlimit(10000)
T = int(input())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    # visited 안 쓰는 방법
    # 배추가 있는 경우(1)에 방문하므로 0으로 변경해 배추가 없다고 본다
    arr[r][c] = 0
    # 상우하좌 방향으로 연결된 부분 탐색, 배추가 있는 경우(1)에만 다시 dfs 수행
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0<=nr<N and 0<=nc<M and arr[nr][nc]:
            dfs(nr, nc)
    return True

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, sys.stdin.readline().split())
        arr[r][c] = 1
    cnt = 0
    for r in range(N):
        for c in range(M):
            # 배추가 있는 땅(1)에서만 dfs 수행
            if arr[r][c] and dfs(r, c):
                # 하나의 연결된 부분을 모두 탐색 완료, 카운트 하나 추가
                cnt += 1
    print(cnt)
import sys
sys.stdin = open('swea_2382.txt')

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
opp = [0, 2, 1, 4, 3]
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [[[0, 0, 0]]*N for _ in range(N)]
    narr = [[[0, 0, 0]]*N for _ in range(N)]
    for _ in range(K):
        r, c, num, dir = map(int, input().split())
        arr[r][c] = [num, dir, num]
    for _ in range(M):
        for r in range(N):
            for c in range(N):
                if arr[r][c][0] == 0: continue
                nr, nc = r + dr[arr[r][c][1]], c + dc[arr[r][c][1]]
                if nr == 0 or nr == N-1 or nc == 0 or nc == N-1:
                    arr[r][c][0] //= 2
                    arr[r][c][1] = opp[arr[r][c][1]]
                if 0<=nr<N and 0<=nc<N:
                    if not narr[nr][nc][0]:
                        narr[nr][nc] = arr[r][c]
                    elif narr[nr][nc][2] > arr[r][c][0]:
                        narr[nr][nc][0] += arr[r][c][0]
                    else:
                        narr[nr][nc][2] = arr[r][c][0]
                        narr[nr][nc][0] += arr[r][c][0]
                        narr[nr][nc][1] = arr[r][c][1]
        for r in range(N):
            for c in range(N):
                arr[r][c] = narr[r][c]
                arr[r][c][2] = arr[r][c][0]
                narr[r][c] = [0, 0, 0]
    ans = 0
    for r in range(N):
        for c in range(N):
            ans += arr[r][c][0]
    print(f'#{tc} {ans}')
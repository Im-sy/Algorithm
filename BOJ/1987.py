import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

visited = [0]*26
ans = 0
def dfs(r, c, cnt):
    global ans
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0<=nr<R and 0<=nc<C:
            idx = ord(board[nr][nc])-65
            if not visited[idx]:
                visited[idx] = 1
                dfs(nr, nc, cnt+1)
                visited[idx] = 0
    ans = max(ans, cnt)

visited[ord(board[0][0])-65] = 1
dfs(0, 0, 1)
print(ans)
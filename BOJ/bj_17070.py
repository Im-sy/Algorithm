import sys
input = sys.stdin.readline

N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]

def dfs(x, y, z):
    global cnt
    if x == N-1 and y == N-1:
        cnt += 1
        return
    if z == 0 or z == 2:
        if y+1 < N and home[x][y+1] == 0:
            dfs(x, y+1, 0)
    if z == 1 or z == 2:
        if x+1 < N and home[x+1][y] == 0:
            dfs(x+1, y, 1)
    if x+1 < N and y+1 < N and home[x][y+1] == 0 and home[x+1][y] == 0 and home[x+1][y+1] == 0:
        dfs(x+1, y+1, 2)

cnt = 0
dfs(0, 1, 0)
print(cnt)
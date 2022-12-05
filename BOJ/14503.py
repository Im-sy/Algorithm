import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def getdir(d):
    if d == 0:
        return [3, 2, 1, 0]
    elif d == 1:
        return [0, 3, 2, 1]
    elif d == 2:
        return [1, 0, 3, 2]
    elif d == 3:
        return [2, 1, 0, 3]

maps[r][c] = -1
cnt = 1
while True:
    nd = getdir(d)
    for x in nd:
        nr = r + dr[x]
        nc = c + dc[x]
        if not maps[nr][nc]:
            r = nr
            c = nc
            maps[nr][nc] = -1
            cnt += 1
            d = x
            break
    else:
        r -= dr[x]
        c -= dc[x]
        if maps[r][c] == 1:
            break
print(cnt)
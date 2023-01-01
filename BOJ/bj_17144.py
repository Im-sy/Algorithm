import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
arrs = [list(map(int, input().split())) for _ in range(R)]

aircon = []
for r in range(R):
    if arrs[r][0] == -1:
        aircon.append(r)

def move_dust():
    dust = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            cnt = 0
            if arrs[r][c]>0:
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < R and 0 <= nc < C and arrs[nr][nc] != -1:
                        dust[nr][nc] += arrs[r][c] // 5
                        cnt += 1
                dust[r][c] -= (arrs[r][c] // 5)*cnt
    for r in range(R):
        for c in range(C):
            arrs[r][c] += dust[r][c]

def air_up():
    sr, sc = aircon[0], 1
    dir1 = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    d = 0
    tmp = 0
    cr, cc = sr, sc
    while True:
        nr, nc = cr + dir1[d][0], cc + dir1[d][1]
        if cr == sr and cc == 0:
            break
        if 0<=nr<R and 0<=nc<C:
            arrs[cr][cc], tmp = tmp, arrs[cr][cc]
            cr, cc = nr, nc
        else:
            d += 1

def air_down():
    sr, sc = aircon[1], 1
    dir2 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0
    tmp = 0
    cr, cc = sr, sc
    while True:
        nr, nc = cr + dir2[d][0], cc + dir2[d][1]
        if cr == sr and cc == 0:
            break
        if 0 <= nr < R and 0 <= nc < C:
            arrs[cr][cc], tmp = tmp, arrs[cr][cc]
            cr, cc = nr, nc
        else:
            d += 1

for _ in range(T):
    move_dust()
    air_up()
    air_down()

ans = 0
for r in range(R):
    for c in range(C):
        if arrs[r][c]>0:
            ans += arrs[r][c]
print(ans)
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def aircheck():
    q = deque()
    q.append((0, 0))
    air[0][0] = -1
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            di = ci + dr[k]
            dj = cj + dc[k]
            if 0<=di<N and 0<=dj<M and air[di][dj] == 0:
                air[di][dj] = -1
                q.append((di, dj))

def ismelting(i, j):
    cnt = 0
    for k in range(4):
        di = i + dr[k]
        dj = j + dc[k]
        if air[di][dj] == -1:
            cnt += 1
    if cnt >= 2:
        return True
    else:
        return False

def solve():
    q = deque()
    for r in range(N):
        for c in range(M):
            if cheese[r][c] == 1 and ismelting(r, c):
                q.append((r, c))
    while q:
        r, c = q.popleft()
        cheese[r][c] = 0


ans = 0
while True:
    one = []
    for r in range(N):
        for c in range(M):
            if cheese[r][c] == 1:
                one.append((r, c))
    air = deepcopy(cheese)
    aircheck()
    if one:
        solve()
        ans += 1
    else:
        break
    # for row in cheese:
    #     print(*row)
    # print("=============")

print(ans)
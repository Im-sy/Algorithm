import sys
from collections import deque
input = sys.stdin.readline

def solve(n, d):
    q = deque([(n, d)])
    v = [0]*5
    v[n] = 1
    path = []
    while q:
        cn, cd = q.popleft()
        path.append((cn, cd))
        if cn >= 2 and gears[cn][-2] != gears[cn-1][2] and not v[cn-1]:
            q.append((cn-1, cd*(-1)))
            v[cn-1] = 1
        if 0< cn <= 3 and gears[cn][2] != gears[cn+1][-2] and not v[cn+1]:
            q.append((cn+1, cd*(-1)))
            v[cn+1] = 1
    return path


gears = [0] + [deque(list(map(int, input().strip()))) for _ in range(4)]
K = int(input())
for _ in range(K):
    num, dir = map(int, input().split())
    turn = solve(num, dir)
    # print(turn)
    for n, d in turn:
        if d == 1:
            gears[n].insert(0, gears[n].pop())
        else:
            gears[n].append(gears[n].popleft())
    # for g in gears:
    #     print(g)
ans = 0
for i in range(1, 5):
    if gears[i][0]:
        ans += 2**(i-1)
print(ans)
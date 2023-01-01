import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []
for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            home.append((r, c))
        elif city[r][c] == 2:
            chicken.append((r, c))

ans = sys.maxsize
for chick in combinations(chicken, M):
    tmp = 0
    for h_x, h_y in home:
        dist = sys.maxsize
        for c_x, c_y in chick:
            dist = min(dist, abs(h_x - c_x)+abs(h_y - c_y))
        tmp += dist
    ans = min(ans, tmp)
print(ans)
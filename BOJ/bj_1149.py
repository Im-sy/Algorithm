import sys
input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
rgb = [[0, 0, 0] for _ in range(N)]
rgb[0] = costs[0]
for i in range(1, N):
    rgb[i][0] = min(rgb[i - 1][1], rgb[i - 1][2]) + costs[i][0]
    rgb[i][1] = min(rgb[i - 1][0], rgb[i - 1][2]) + costs[i][1]
    rgb[i][2] = min(rgb[i - 1][0], rgb[i - 1][1]) + costs[i][2]

print(min(rgb[N-1]))
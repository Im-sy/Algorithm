import sys
N = int(sys.stdin.readline())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = [[0]*N for _ in range(N)]

from collections import deque

def bfs(n):
    q = deque()
    q.append(n)
    v = [0]*N
    while q:
        ci = q.popleft()
        for k in range(N):
            if edges[ci][k] and not v[k]:
                q.append(k)
                v[k] = 1
    print(*v)


for i in range(N):
    bfs(i)

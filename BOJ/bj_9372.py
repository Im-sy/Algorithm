import sys
from collections import deque
T = int(sys.stdin.readline())
for tc in range(T):
    N, M = map(int, sys.stdin.readline().split())
    edges = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        edges[a].append(b)
        edges[b].append(a)

    q = deque()
    v = [0]*(N+1)
    q.append(1)
    v[1] = 1
    cnt = 0
    while q:
        current = q.popleft()
        for x in edges[current]:
            if not v[x]:
                q.append(x)
                v[x] = 1
                cnt += 1
    print(cnt)
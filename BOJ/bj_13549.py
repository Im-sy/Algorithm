N, K = map(int, input().split())
from collections import deque

def solve(n):
    global ans
    q = deque()
    v = [0] * 100001
    q.append((n, 0))
    v[n] = 1
    while q:
        c, d = q.popleft()
        if c == K and ans > d:
            ans = d
            return
        # 순간이동(2배)
        if 0<=2*c<100001 and not v[2*c]:
            q.append((2*c, d))
            v[2*c] = 1
        # 좌우이동
        for nc in [c-1, c+1]:
            if 0<=nc<100001 and not v[nc]:
                q.append((nc, d+1))
                v[nc] = 1

ans = float('INF')
solve(N)
print(ans)
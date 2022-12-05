import sys
input = sys.stdin.readline
from collections import deque

def bfs(n):
    q = deque([n])
    v = [0]*(N+1)
    v[n] = 1
    cnt = 1
    while q:
        cn = q.popleft()
        for nn in coms[cn]:
            if not v[nn]:
                q.append(nn)
                v[nn] = 1
                cnt += 1
    return cnt

N, M = map(int, input().split())
coms = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    coms[B].append(A)

res = [0]
for i in range(1, N+1):
    res.append(bfs(i))
max_res = max(res)
# print(res)
for i in range(1, N+1):
    if res[i]==max_res:
        print(i, end=' ')
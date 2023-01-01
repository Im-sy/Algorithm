# def solve(n, cnt):
#     if n == M:
#         result.append(cnt)
#         return
#     if 1 <= n+1 <= 1000000 and not visited[n+1]:
#         visited[n+1] = 1
#         solve(n + 1, cnt + 1)
#     if 1 <= n-1 <= 1000000 and not visited[n-1]:
#         visited[n-1] = 1
#         solve(n - 1, cnt + 1)
#     if 1 <= n*2 <= 1000000 and not visited[n*2]:
#         visited[n*2] = 1
#         solve(n * 2, cnt + 1)
#     if 1 <= n-10 <= 1000000 and not visited[n-10]:
#         visited[n-10] = 1
#         solve(n - 10, cnt + 1)

from collections import deque

def bfs(v):
    q = deque()
    q.append((v, 0))
    visited = [0]*1000001
    visited[v] = 1
    while q:
        current, cnt = q.popleft()
        if current == M:
            return cnt
        if 1 <= current+1 <= 1000000 and not visited[current+1]:
            q.append((current+1, cnt+1))
            visited[current+1] = 1
        if 1 <= current-1 <= 1000000 and not visited[current-1]:
            q.append((current-1, cnt+1))
            visited[current-1] = 1
        if 1 <= current*2 <= 1000000 and not visited[current*2]:
            q.append((current*2, cnt+1))
            visited[current*2] = 1
        if 1 <= current-10 <= 1000000 and not visited[current-10]:
            q.append((current-10, cnt+1))
            visited[current-10] = 1

import sys
sys.setrecursionlimit(10**6)
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # result = []
    # visited = [0]*1000001
    # visited[N] = 1
    # solve(N, 0)
    # print(f'#{tc} {min(result)}')
    print(f'#{tc} {bfs(N)}')
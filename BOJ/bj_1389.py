import sys
N, M = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    arr[A].append(B)
    arr[B].append(A)

from collections import deque

def bfs(n):
    q = deque()
    visited = [0]*(N+1)
    q.append(n)
    visited[n] = 1
    while q:
        c = q.popleft()
        for x in arr[c]:
            if not visited[x]:
                q.append(x)
                visited[x] = visited[c] + 1
    return sum(visited)

ans = []
for i in range(1, N+1):
    ans.append(bfs(i))
print(ans.index(min(ans))+1)

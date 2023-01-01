import sys
input = sys.stdin.readline
N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

visited = [0]*(N+1)
def dfs(n):
    stack = [n]
    visited[n] = 1
    while stack:
        top = stack.pop(0)
        for x in edges[top]:
            if not visited[x]:
                stack.append(x)
                visited[x] = 1

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)
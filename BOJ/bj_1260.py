import sys
N, M, V = map(int, sys.stdin.readline().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    arr[start][end] = 1
    arr[end][start] = 1

def dfs():
    visited = [0] * (N + 1)
    stack = [V]
    visited[V] = 1
    print(V, end=' ')
    while stack:
        # current = stack[-1]
        current = stack.pop()
        for i in range(1, N+1):
            if arr[current][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                print(i, end=' ')
                break
                # break 없이
        # else:
        #     stack.pop()

def bfs():
    visited = [0]*(N+1)
    queue = [V]
    visited[V] = 1
    while queue:
        current = queue.pop(0)
        print(current, end=' ')
        for i in range(1, N+1):
            if arr[current][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1

dfs()
print()
bfs()

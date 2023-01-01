import sys
N, M = map(int, sys.stdin.readline().split())
board = [0]*101
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    board[x] = y
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    board[u] = v


from collections import deque
ans = 100
v = [0] * 101

def bfs(n):
    q = deque()
    q.append(n)
    v[n] = 1
    while q:
        current = q.popleft()
        for k in range(1, 7):
            next = current + k
            if 1 <= next <= 100:
                if board[next]:
                    next = board[next]
                if not v[next]:
                    q.append(next)
                    v[next] = v[current] + 1
bfs(1)
print(v[100]-1)
import sys
from collections import deque
# 나이트 이동 방향(시계방향)
dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    I = int(sys.stdin.readline())
    sr, sc = map(int, sys.stdin.readline().split())
    er, ec = map(int, sys.stdin.readline().split())
    
    # BFS 수행
    q = deque()
    q.append((sr, sc, 0))
    v = [[0]*I for _ in range(I)]
    v[sr][sc] = 1
    while q:
        cr, cc, d = q.popleft()
        # 끝점에 도달하면 break
        if cr == er and cc == ec:
            break
        # 나이트 이동방향으로
        for k in range(8):
            nr = cr + dr[k]
            nc = cc + dc[k]
            # 범위 내에 있고 방문하지 않은 경우
            if 0<=nr<I and 0<=nc<I and not v[nr][nc]:
                q.append((nr, nc, d+1))
                v[nr][nc] = 1
    print(d)
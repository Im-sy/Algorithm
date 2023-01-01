import sys
N, M = map(int, input().split())
maze = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
# 행 열 칸수
start = (0, 0, 1)
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
queue = [start]
while queue:
    cr, cc, d = queue.pop(0)
    # (N-1, M-1) 위치에 도달하면 도착
    if cr == N-1 and cc == M-1:
        break
    # 상우하좌 모든 방향에 대해서 이동할 수 있고(1) 방문하지 않은 곳 탐색
    for k in range(4):
        nr = cr + dr[k]
        nc = cc + dc[k]
        if 0<=nr<N and 0<=nc<M and maze[nr][nc] and not visited[nr][nc]:
            # 갈 수 있는 곳을 enqueue할 때 칸수 하나 더해주기
            queue.append((nr, nc, d+1))
            visited[nr][nc] = 1
print(d)
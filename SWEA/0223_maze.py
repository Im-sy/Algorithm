mazearr = [
    [2,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,1],
    [1,1,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,3]
]
# DFS = 현 상태에서 가능한 모든 경우의 수 고려
# 현재 위치 (r, c) -> 현재 위치에서 갈 수 있는 경우의 수 모두 찾기
r, c = 0, 0
N = 8
stack = []
stack.append((r, c))
visited = [[0]*N for _ in range(N)]
visited[r][c] = 1
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 현재위치(top)에서 갈 수 있는 경로 탐색
# 경로 찾으면 push, 방문표시, 즉시이동(break)
# 경로 없으면 pop
# stack 빌 때 까지 반복
while stack:
    cr, cc = stack[-1]
    # cr, cc = stack.pop()
    if mazearr[cr][cc] == 3:
        print('길 찾음')
        break
    for d in range(4):
        nr = cr + dr[d]
        nc = cc + dc[d]
        if 0<=nr<N and 0<=nc<N and mazearr[nr][nc]!=1 and not visited[nr][nc]:
            stack.append((nr, nc))
            visited[nr][nc] = 1
            break
    else:
        stack.pop()
    # else 없이
    # stack.pop()
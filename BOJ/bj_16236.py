# BFS
# fish 리스트에 먹을 수 있는 물고기 행,열,이동거리 저장
# 상우하좌 탐색
# 물고기 크기가 아기상어 크기보다 작을 때 fish에 추가+이동(q)
# 물고기 크기가 아기상어 크키와 같거나 물고기가 없는 영역일 땐 그냥 이동만
# fish 다 찾았으면 이동거리 순으로 정렬해서 제일 작은 것만 return

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


import sys
from collections import deque
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for r in range(N):
    for c in range(N):
        if arr[r][c] == 9:
            sr, sc = r, c
            arr[sr][sc] = 0
            break

def bfs(r, c, size):
    q = deque()
    q.append((r, c, 0))
    visited = [[0]*N for _ in range(N)]
    visited[r][c] = 1
    fish = []
    while q:
        cr, cc, d = q.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                if arr[nr][nc] and arr[nr][nc] < size:
                    fish.append((nr, nc, d+1))
                    q.append((nr, nc, d+1))
                    visited[nr][nc] = 1
                elif not arr[nr][nc] or arr[nr][nc] == size:
                    q.append((nr, nc, d+1))
                    visited[nr][nc] = 1
    if fish:
        fish.sort(key=lambda x: (x[2], x[0], x[1]))
        return fish[0]
    else:
        return []



# 9 부터 시작(아기상어 존재하는 곳)
# BFS 돌고 오면 현재에서 가장 가까운 물고기 먹는다
# 이동 거리를 결과값에 더해주고 위치를 변경
# 물고기 먹으면 값 0으로 바꾸고 먹은 물고기 개수(eat) 증가
# eat이 아기상어 현재 크기와 같아지면 아기상어 크기 +1, eat은 0으로 초기화
# 더이상 먹을 수 있는 물고기가 없으면 break


size = 2
eat = 0
ans = 0
while True:
    fish = bfs(sr, sc, size)
    if fish:
        r, c, dist = fish
        arr[r][c] = 0
        eat += 1
        ans += dist
        if eat == size:
            size += 1
            eat = 0
        sr, sc = r, c
    else:
        break
print(ans)
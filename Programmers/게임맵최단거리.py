from collections import deque


def solution(maps):
    # answer = 0
    n = len(maps)
    m = len(maps[0])
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    def bfs(r, c):
        q = deque([(r, c, 0)])
        v = [[0]*m for _ in range(n)]
        v[r][c] = 1
        while q:
            cr, cc, path = q.popleft()
            if cr == n-1 and cc == m-1:
                return path+1
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if 0<=nr<n and 0<=nc<m and maps[nr][nc]==1 and not v[nr][nc]:
                    q.append((nr, nc, path+1))
                    v[nr][nc] = 1
        return -1

    answer = bfs(0, 0)

    return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
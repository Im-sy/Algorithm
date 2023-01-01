import sys
sys.stdin = open('swea_1226.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for _ in range(10):
    tc = int(input())
    print(f'#{tc}', end=' ')
    maze = [list(input()) for _ in range(16)]
    for r in range(16):
        for c in range(16):
            if maze[r][c] == '2':
                start = (r, c)
                break
    visited = [[0]*16 for _ in range(16)]
    stack = [start]
    visited[start[0]][start[1]] = 1
    while stack:
        cr, cc = stack.pop()
        if maze[cr][cc] == '3':
            print(1)
            break
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0<=nr<16 and 0<=nc<16 and maze[nr][nc]!='1' and not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = 1
    else:
        print(0)

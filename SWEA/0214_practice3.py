N = 5
r = c = 0
dir = 0
dr = [0, 1, 0, -1] #우하좌상
dc = [1, 0, -1, 0]
arr = [[0]*N for _ in range(N)]
for cnt in range(1, N*N+1):
    arr[r][c] = cnt
    r += dr[dir]
    c += dc[dir]
    if r<0 or c<0 or r>=N or c>=N or arr[r][c]:
        r -= dr[dir]
        c -= dc[dir]
        dir = (dir+1) % 4
        r += dr[dir]
        c += dc[dir]
# 교수님 풀이
num = 1
while num <= N*N:
    if 0<=r<N and 0<=c<N and not arr[r][c]: # 정상 범위
        arr[r][c] = num
        num += 1
    else:
        # 일단 정상 범위 안으로 돌려보내고
        r -= dr[dir]
        c -= dr[dir]
        # 방향 전환
        dir = (dir+1) % 4
    r += dr[dir]
    c += dr[dir]



for row in arr:
    print(row)
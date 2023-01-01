import sys
N = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().rstrip('\n'))) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 단지수도 인수로 받음
def dfs(cnt, r, c):
    # visited 없이 수행하는 방법
    # 아파트가 있는 경우(1)에 탐색되므로 0으로 변경해서 아파트가 없다고 본다
    arr[r][c] = 0
    # 상우하좌 방향으로 아파특가 있는 경우에 다시 dfs 탐색
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0<=nr<N and 0<=nc<N and arr[nr][nc]:
            # 단지수는 하나 더해주기
            cnt = dfs(cnt+1, nr, nc)
    return cnt

ans = []
for r in range(N):
    for c in range(N):
        # 아파트가 있다면 dfs 시작
        if arr[r][c]:
            # 모두 탐색하고 얻은 단지수 값을 ans 리스트에 저장
            ans.append(dfs(1, r, c))

# 몇 단지인지, 각 단지수를 오름차순으로 출력
print(len(ans))
for x in sorted(ans):
    print(x)
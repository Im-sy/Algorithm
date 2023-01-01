def solve(idx, tmp):
    global ans
    if ans <= tmp:
        return
    if idx==N and ans > tmp:
        ans = tmp
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            solve(idx+1, tmp+arr[idx][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 100*N
    visited = [0]*N
    solve(0, 0)
    print(f'#{tc} {ans}')
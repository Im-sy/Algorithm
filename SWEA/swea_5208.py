def solve(n, cnt):
    global ans
    if ans <= cnt:
        return
    if n >= N-1:
        if ans > cnt:
            ans = cnt
        return
    # print(arr[n], cnt)
    for i in range(1, arr[n]+1):
        solve(n+i, cnt+1)

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split())) + [0]
    N = arr.pop(0)
    # print(N, arr)
    ans = 99999999
    solve(0, -1)
    print(f'#{tc} {ans}')

def dfs(n, ssum):
    global ans
    if n > 12:
        if ans > ssum:
            ans = ssum
        return
    dfs(n + 1, ssum + lst[n]*day)
    dfs(n + 1, ssum * mon)
    dfs(n + 3, ssum * mon3)
    dfs(n + 12, ssum * year)


T = int(input())
for tc in range(1, T+1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0]+list(map(int, input().split()))
    ans = 99999999
    dfs(1, 0)
    print(f'#{tc} {ans}')

    # 다른 풀이 (이전달에서 누적합해서 가장 작게)
    D = [0]*13
    for i in range(1, 13):
        mmin = D[i-1] + lst[i]*day
        mmin = min(mmin, D[i-1] + mon)
        if i >= 3:
            mmin = min(mmin, D[i-3] + mon3)
        if i >= 12:
            mmin = min(mmin, D[i-12] + year)
        D[i] = mmin
    print(f'#{tc} {D[12]}')
def solve(n, i, j):
    global cnt
    if i == r and j == c:
        print(cnt)
        exit(0)
    if n==1:
        cnt += 1
        return
    # 시간 줄이기
    if not (i <= r < i + n and j <= c < j + n):
        cnt += n * n
        return
    nn = n//2
    solve(nn, i, j)
    solve(nn, i, j+nn)
    solve(nn, i+nn, j)
    solve(nn, i+nn, j+nn)


import sys
# sys.setrecursionlimit(10**6)
N, r, c = map(int, sys.stdin.readline().split())
cnt = 0
solve(2**N, 0, 0)
print(cnt)
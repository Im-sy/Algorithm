def solve(n):
    global cnt
    if n > N:
        return
    if n == N:
        cnt += 1
        return
    solve(n+1)
    solve(n+2)
    solve(n+3)

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cnt = 0
    solve(0)
    print(cnt)
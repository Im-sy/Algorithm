# swea 4012 요리사 문제와 유사함
def dfs(n, A, B):
    global ans
    if len(A) > N//2 or len(B) > N//2:
        return
    if n == N:
        if len(A) == len(B):
            asum, bsum = 0, 0
            for i in range(N//2):
                for j in range(N//2):
                    asum += arr[A[i]][A[j]]
                    bsum += arr[B[i]][B[j]]
            if ans > abs(asum-bsum):
                ans = abs(asum-bsum)
        return
    dfs(n+1, A+[n], B)
    dfs(n+1, A, B+[n])

import sys
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 10**7
dfs(0, [], [])
print(ans)
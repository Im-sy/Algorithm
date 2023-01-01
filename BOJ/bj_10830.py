import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# A^B % 1000
# 1629
# from operator import matmul
def matmul(a, b):
    mul = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            tmp = 0
            for i in range(N):
                tmp += a[r][i] * b[i][c]
            mul[r][c] = tmp%1000
    return mul

def solve(a, b):
    if b == 1:
        for r in range(N):
            for c in range(N):
                a[r][c] %= 1000
        return a
    tmp = solve(a, b//2)
    if b%2:
        return matmul(matmul(tmp, tmp), a)
    else:
        return matmul(tmp, tmp)

for row in solve(A, B):
    print(*row)
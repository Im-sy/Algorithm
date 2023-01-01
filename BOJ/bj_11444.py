N = int(input())
mod = 1000000007

def matmul(a, b):
    M = len(b[0])
    mul = [[0]*M for _ in range(2)]
    for r in range(2):
        for c in range(M):
            tmp = 0
            for i in range(2):
                tmp += a[r][i] * b[i][c]
            mul[r][c] = tmp%mod
    return mul
    # n = len(a)
    # mul = [[0]*n for _ in range(n)]
    # for r in range(n):
    #     for c in range(n):
    #         tmp = 0
    #         for i in range(n):
    #             tmp += a[r][i] * b[i][c]
    #         mul[r][c] = tmp%1000
    # return mul

def solve(a, b):
    if b == 1:
        return a
    if b%2:
        return matmul(solve(a, b-1), a)
    else:
        return solve(matmul(a, a), b//2)
    # if b == 1:
    #     for r in range(len(a)):
    #         for c in range(len(a)):
    #             a[r][c] %= mod
    #     return a
    # tmp = solve(a, b // 2)
    # if b % 2:
    #     return matmul(matmul(tmp, tmp), a)
    # else:
    #     return matmul(tmp, tmp)

if N<=2:
    print(1)
else:
    print(matmul(solve([[1, 1], [1, 0]], N-2), [[1], [1]])[0][0])
# print(solve([[1, 1], [1, 0]], N)[0][1])
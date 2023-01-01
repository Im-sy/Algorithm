def solve(n, r, c):
    if n == 1:
        return arr[r][c]
    nn = n//2
    lu = solve(nn, r, c)
    ru = solve(nn, r, c+nn)
    ld = solve(nn, r+nn, c)
    rd = solve(nn, r+nn, c+nn)
    if lu==ru==ld==rd and len(lu)==1:
        return lu
    return lu+ru+ld+rd


import sys
N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().split()) for _ in range(N)]
ans = solve(N, 0, 0)
# print(ans)
print(ans.count('0'))
print(ans.count('1'))

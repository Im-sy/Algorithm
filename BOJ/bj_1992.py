# import sys
# N = int(sys.stdin.readline().strip())
# arr = [sys.stdin.readline().strip() for _ in range(N)]
#
# def solve(n, r, c):
#     if n == 1:
#         return arr[r][c]
#     cnt = 0
#     for i in range(r, r + n):
#         for j in range(c, c + n):
#             cnt += int(arr[i][j])
#     if cnt == 0:
#         return '0'
#     elif cnt == n ** 2:
#         return '1'
#     lu = solve(n//2, r, c)
#     ru = solve(n//2, r, c+n//2)
#     ld = solve(n//2, r+n//2, c)
#     rd = solve(n//2, r+n//2, c+n//2)
#     return f'({lu + ru + ld + rd})'
#
# ans = solve(N, 0, 0)
# print(ans)

#
# import sys
#
# N = int(sys.stdin.readline().strip())
# arr = [sys.stdin.readline().strip() for _ in range(N)]
#
# def check(path):
#     for p in path:
#         if p == '(':
#             return path
#         if p != '1':
#             break
#     else:
#         return '1'
#     for p in path:
#         if p != '0':
#             break
#     else:
#         return '0'
#     return f'({path})'
#
#
# def solve(n, r, c):
#     if n == 1:
#         return arr[r][c]
#     lu = solve(n // 2, r, c)
#     ru = solve(n // 2, r, c + n // 2)
#     ld = solve(n // 2, r + n // 2, c)
#     rd = solve(n // 2, r + n // 2, c + n // 2)
#     if lu == ru == ld == rd and len(lu) == 1:
#         return lu
#     return f'({lu+ru+ld+rd})'
#
#
# # ans = f'({solve(N, 0, 0)})'
# # if ans == '(1111)' or ans == '(1)':
# #     ans = '1'
# # if ans == '(0000)' or ans == '(0)':
# #     ans = '0'
#
# ans = solve(N, 0, 0)
#
# print(ans)


import sys

N = int(sys.stdin.readline().strip())
arr = [sys.stdin.readline().strip() for _ in range(N)]

def check(path):
    for p in path:
        if p == '(':
            return path
        if p != '1':
            break
    else:
        return '1'
    for p in path:
        if p != '0':
            break
    else:
        return '0'
    return f'({path})'


def solve(n, r, c):
    if n == 1:
        return arr[r][c]
    lu = solve(n // 2, r, c)
    ru = solve(n // 2, r, c + n // 2)
    ld = solve(n // 2, r + n // 2, c)
    rd = solve(n // 2, r + n // 2, c + n // 2)
    return check(lu) + check(ru) + check(ld) + check(rd)


ans = f'({solve(N, 0, 0)})'
if ans == '(1111)' or ans == '(1)':
    ans = '1'
if ans == '(0000)' or ans == '(0)':
    ans = '0'
print(ans)
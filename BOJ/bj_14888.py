def permutation(idx, perm, selected):
    global M, m
    if idx == N-1:
        tmp = arr[0]
        for i in range(1, N):
            if perm[i-1] == '+':
                tmp += arr[i]
            elif perm[i-1] == '-':
                tmp -= arr[i]
            elif perm[i-1] == '*':
                tmp *= arr[i]
            elif perm[i-1] == '/':
                tmp = int(tmp/arr[i])
        if tmp > M:
            M = tmp
        if tmp < m:
            m = tmp
        return
    for i in range(N-1):
        if not selected[i]:
            perm[idx] = cal[i]
            selected[i] = 1
            permutation(idx+1, perm, selected)
            selected[i] = 0

import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
a, b, c, d = map(int, sys.stdin.readline().split())
cal = ['+']*a + ['-']*b + ['*']*c + ['/']*d
M = -10000000000
m = 10000000000
# permutation(0, [0]*(N-1), [0]*(N-1))
# print(M)
# print(m)

# from itertools import permutations
# # print(list(permutations(cal, N-1)))
# for perm in permutations(cal, N-1):
#     tmp = arr[0]
#     for i in range(1, N):
#         if perm[i - 1] == '+':
#             tmp += arr[i]
#         elif perm[i - 1] == '-':
#             tmp -= arr[i]
#         elif perm[i - 1] == '*':
#             tmp *= arr[i]
#         elif perm[i - 1] == '/':
#             tmp = int(tmp / arr[i])
#     if tmp > M:
#         M = tmp
#     if tmp < m:
#         m = tmp
#
# print(M)
# print(m)

op = list(map(int, sys.stdin.readline().split()))
def dfs(idx, tmp, plus, minus, multiply, divide):
    global M, m
    if idx == N:
        M = max(tmp, M)
        m = min(tmp, m)
        return
    if plus:
        dfs(idx+1, tmp+arr[idx], plus-1, minus, multiply, divide)
    if minus:
        dfs(idx+1, tmp-arr[idx], plus, minus-1, multiply, divide)
    if multiply:
        dfs(idx+1, tmp*arr[idx], plus, minus, multiply-1, divide)
    if divide:
        dfs(idx+1, int(tmp/arr[idx]), plus, minus, multiply, divide-1)
dfs(1, arr[0], op[0], op[1], op[2], op[3])
print(M)
print(m)
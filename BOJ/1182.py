import sys
input = sys.stdin.readline
from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))

# cnt = 0
# for i in range(1, N+1):
#     for comb in combinations(arr, i):
#         if sum(comb) == S:
#             cnt += 1
# print(cnt)

def solve(sel, idx, level, r):
    global cnt
    if level == r:
        tmp = 0
        for i in range(N):
            if sel[i]:
                tmp += arr[i]
        if tmp == S:
            cnt += 1
        return
    if idx >= N:
        return
    sel[idx] = 1
    solve(sel, idx+1, level+1, r)
    sel[idx] = 0
    solve(sel, idx+1, level, r)

cnt = 0
for i in range(1, N+1):
    solve([0]*N, 0, 0, i)

print(cnt)
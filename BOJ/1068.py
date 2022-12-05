import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
parent = list(map(int, input().split()))
rem = int(input())

# def solve(n):
#     q = deque([n])
#     parent[n] = -1
#     while q:
#         cn = q.popleft()
#         for i in range(N):
#             if parent[i] == cn:
#                 q.append(i)
#                 parent[i] = -1

def solve(n):
    parent[n] = -2
    for i in range(N):
        if n == parent[i]:
            solve(i)

solve(rem)

cnt = 0
for i in range(N):
    if parent[i] != -2 and i not in parent:
        cnt += 1
print(cnt)

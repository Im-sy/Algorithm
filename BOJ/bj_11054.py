import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
dp = [0]*N
dpl = [0]*N
dpr = [0]*N
for i in range(N):
    for j in range(i):
        if A[i]>A[j] and dpl[i]<dpl[j]:
            dpl[i] = dpl[j]
    dpl[i] += 1
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[i]>A[j] and dpr[i]<dpr[j]:
            dpr[i] = dpr[j]
    dpr[i] += 1
for i in range(N):
    dp[i] = dpl[i] + dpr[i] - 1
print(max(dp))
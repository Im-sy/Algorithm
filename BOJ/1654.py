import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lengths = sorted([int(input().strip()) for _ in range(K)])

ans = 0
l = 1
r = lengths[K-1]
while l<=r:
    m = (l+r)//2
    cnt = 0
    for i in range(K):
        cnt += lengths[i] // m
    if cnt >= N:
        ans = max(ans, m)
        l = m+1
    else:
        r = m-1

print(ans)